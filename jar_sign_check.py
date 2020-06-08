# Tool to recursively check if jar files are digitally signed
# Ouput is written to stdout and the output is written to files
# Output files, signed.txt & unsigned.txt are written in the folder that the script is run
# Script needs to be run in the top level folder of the application that is being checked
# sh3llcmdr
# 31 Oct 2019

#imports
import os
import os.path
import subprocess
from sys import platform
import datetime

#variables
jarsigner_loc = "C:\\Program files\\Java\\jdk1.8.0_231\\bin\\"
cmd = jarsigner_loc + "jarsigner.exe -verify "

# OS check
if platform == "win32":
    os.system("cls")
elif platform == "linux":
    os.system("clear")

#get date for datestamp
now = datetime.datetime.now()

# Welcome message
print("=================================================================")
print("sh3llcmdr - jar_sign_check.py")
print("Tool to recursively check if a jar files are signed")
print("Check output.txt in this folder for output from signed jar files")
print("Testing jar files in current folder and subdirectories")
print("=================================================================")

# Create and open the output file for signed files
signedtxt = open("signed.txt", "w+")
signedtxt.write("jar_sign_check.py\n")
signedtxt.write("sh3llcmdr - jar_sign_check.py\n")
signedtxt.write(str(now.strftime("%d-%m-%Y %H:%M")) + "\n")
signedtxt.write("Below are the signed jar files with the output from jarsigner\n")
signedtxt.write("=====================================\n")

# Create and open the output file for unsigned files
unsignedtxt = open("unsigned.txt", "w+")
unsignedtxt.write("jar_sign_check.py\n")
unsignedtxt.write("sh3llcmdr - jar_sign_check.py\n")
unsignedtxt.write(str(now.strftime("%d-%m-%Y %H:%M")) + "\n")
unsignedtxt.write("Below are the unsigned jar files with the output from jarsigner\n")
unsignedtxt.write("=====================================\n")

#recursively check the current folder and subs
for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".jar"):
            # catch the output
            test = subprocess.Popen(cmd + root + "\\" + filename,stdout=subprocess.PIPE)
            test_out = test.stdout.read()
            # file location
            fileloc = root + "\\" + filename
            # test the output
            if "jar is unsigned" not in test_out:
                # write to output.txt
                signedtxt.write("=====================================\n" + fileloc + test_out + "\n")
                print("signed: " + fileloc)
            else:
                # write to output.txt
                unsignedtxt.write("=====================================\n" + fileloc + test_out + "\n")
                print("unsigned: " + fileloc)

# output message
print("=================================================================")
print("Done.")
print("Check the output files in the current folder: signed.txt & unsigned.txt")
print("=================================================================")

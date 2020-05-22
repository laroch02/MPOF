'''
Created on 29 juill. 2019

@author: david.larochelle
'''

import sys, getopt
if __name__ == '__main__':
    pass

# default value
StartIdentifier = ""
EndIdentifier = ""
FileToInsert = ""
BaseFile = ""
OutputFile = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"hs:e:i:f:o:")
except getopt.GetoptError:
    print("MergePartOfFile: Replaces the text between specified tags by the content of a separate file.")
    print('MPOF.py -s StartIdentifier -e EndIdentifier -f BaseFile -i FileToInsert -o OutputFile')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print("MergePartOfFile: Replaces the text between specified tags by the content of a separate file.")
        print('MPOF.py -s StartIdentifier -e EndIdentifier -f BaseFile -i FileToInsert -o OutputFile')
        sys.exit()
    elif opt in ("-s"):
        StartIdentifier = str(arg)
    elif opt in ("-e"):
        EndIdentifier = str(arg)
    elif opt in ("-i"):
        FileToInsert = str(arg)
    elif opt in ("-f"):
        BaseFile = str(arg)
    elif opt in ("-o"):
        OutputFile = str(arg)

import os

if (FileToInsert == "" or BaseFile == "" or StartIdentifier == "" or EndIdentifier == ""):
    print("Missing arguments. Aborting.")
    sys.exit()

# If Outputfile is not provided, save changes in BaseFile
if (OutputFile == ""):
    OutputFile = BaseFile

import re

# Read Input file
try:
    f = open(FileToInsert, 'r')
    InputStream = f.read()
    f.close()
except:
    print("Could not read input file " + FileToInsert)
    sys.exit()
# Re-insert tags to input stream.
InputStream = StartIdentifier + "\r\n" + InputStream + "\r\n" + EndIdentifier

# Read Output file
try:
    f = open(BaseFile, 'r')
    OutputStream = f.read()
    f.close()
except:
    print("Could not read output file " + BaseFile)
    sys.exit()   
      

# Create regular expression pattern
chop = re.compile(StartIdentifier+'.*?'+EndIdentifier, re.DOTALL)

# Chop text between #chop-begin and #chop-end
data_chopped = chop.sub(InputStream, OutputStream)

# Test if changes were done successfully
if (data_chopped == OutputStream):
    print("No tags found in basefile. Aborting.")
    sys.exit()

# Save result
try:
    f = open(OutputFile, 'w')
    f.write(data_chopped)
    f.close()
except:
    print("Could not write to file " + BaseFile + ". Aborting.")
    sys.exit()

print ("Changes successfull to file "+ OutputFile)    
#!/bin/sh

Building standalone executable from jargon source

# removing old executables folder 'bin'
rm -rf bin/linux

# building executable with cxfreeze
cxfreeze src/jargon.py

# renaming new folder 'dist' to 'bin'
mv dist bin/linux

# copying CSV file from 'src' to 'bin'
cp src/jargon.csv bin/linux/

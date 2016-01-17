'''
Created on Jul 30, 2014

@author: thor
'''
import sys
sys.path.append('../lib')

import csv
import re
import docx2txt

#csvFile = '/Users/thorbenje/python/pygon/src/jargon.csv'
#fileName= '/Users/thorbenje/python/pygon/src/test.txt'

csvFile = 'jargon.csv'

def read_csv(path):
    reader = csv.reader(open(path, 'r'), delimiter='\t', quotechar='"')
    reader.next()
    data = {}

    for row in reader:
        key = row[0]
        val = row[1]
        data[key] = val

    return data


def fileToArray(fileName):

    # identify file type
    split    = str.split(fileName,".")
    fileType = split[len(split)-1]
    print 'File type is ' + str(fileType) + "."

    if fileType == 'docx':
        text = docx2txt.process(fileName).splitlines()

    else:
        # here: asumming a text file
        text = open(fileName).read().splitlines()

    return text


def search_jargon(dictionary, jargonText):

    for linenumber in range(0, len(jargonText)):
        line = jargonText[linenumber]

        for key in dictionary.keys():
            if re.search(key, line, re.IGNORECASE):
                text = 'Line '+ str(linenumber+1) +': "'+key+'" \n'
                text = text + ' - substitute with "'+dictionary[key]+'"? \n'
                print text


print 'Reading word list ...'
jargonDictionary = read_csv(csvFile)

print 'Reading text file ...'
fileName    = sys.argv[1]
jargonText  = fileToArray(fileName)

print 'Reporting jargon for ' + fileName + ' ...\n\n'
search_jargon(jargonDictionary, jargonText)
    
    

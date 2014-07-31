'''
Created on Jul 30, 2014

@author: thor
'''
import csv

jargonCsv = 'jargon.csv'
jargonFile = 'test.txt'

def read_csv(path):
    
    reader = csv.reader(open(path, 'r'), delimiter=',', quotechar='"')
    reader.next()
    data = {}
     
    for row in reader:
        key = row[0]
        val = row[1]
        data[key] = val
        
    return data

def search_jargon(path, dictionary):
    # open and override report file
    with open(path, 'w') as report:
        report.write('Jargon report for '+jargonFile+'\n\n')
        
        with open(jargonFile) as textfile:
            linenumber = 1
            for line in textfile:
                linenumber = linenumber + 1
                for key in dictionary.keys():
                    if key in line:
                        report.write('Line '+str(linenumber)+': "'+key+'"')
                        report.write(' - substitute with "'+dictionary[key]+'"?')
        
        report.write('\n')
        
if __name__ == '__main__':
    jargonDictionary = read_csv(jargonCsv)
    
    search_jargon('jargon_report.txt', jargonDictionary)

        
    
    

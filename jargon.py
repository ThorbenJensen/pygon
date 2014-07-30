'''
Created on Jul 30, 2014

@author: thor
'''
import csv

def read_csv(filename):
    
    reader = csv.reader(open(filename, 'r'), delimiter=',', quotechar='"')
    reader.next()
    data = {}
     
    for row in reader:
        key = row[0]
        val = row[1]
        data[key] = val
        
    return data
        
if __name__ == '__main__':
    table = read_csv('jargon.csv')
    
    print table['more or less']
    
    

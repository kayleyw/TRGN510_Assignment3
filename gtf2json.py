#!/usr/bin/python
import sys
import fileinput
import csv
import json

gtf_file = sys.argv[1]
output=[]
for each_line_of_text in fileinput.input(gtf_file):
    if each_line_of_text.startswith('#'):
        continue
    line = each_line_of_text.split("\t")
    
    if line[2] == 'gene':
        s = next(csv.reader([line[8]], delimiter=' '))
        record = {}
        record["geneName"] = (s[3]).rstrip(";")
        record["chr"] = line[0]
        record["startPos"] = line[3]
        record["endPos"] = line[4]

        output.append(record)
        
y= json.dumps(output,indent=1)
print(y)

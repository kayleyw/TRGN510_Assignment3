#!/usr/bin/python
import sys
import fileinput
import re

phone_num_file = sys.argv[1]
for each_line_of_text in fileinput.input(phone_num_file):
    area_code = re.findall(r'\((.*?)\)',each_line_of_text)
    print(area_code)

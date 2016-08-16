#!/usr/bin/python

import os, re
import sys
from pygoogle import pygoogle

with open('filess.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()
#print  len(my_list)

i = 1

for line in my_list:
    searching = "filetype:" + line
    g = pygoogle(searching)
    g.pages = 1
    l = g.get_urls()
    bashCommand = "wget " + l[1]
    os.system(bashCommand)

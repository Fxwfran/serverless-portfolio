#!/usr/bin/env python
import sys

filename = sys.argv[1]

with open(filename) as hosts_file:
	host_lines = hosts_file.readlines()

host_urls = []

for line in host_lines:
	host_urls.append(line.split(' ')[1])

with open("parsed_"+filename, "w") as parsed_file:
	parsed_file.writelines(host_urls)

print("Successfully parsed hosts file.")
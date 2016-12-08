from sys import argv
script,f=argv
def print_all(f):
	print f.read()
def print_a_line(line_count,f):
	print line_count,f.readline()
txt =open(f)
print_all(txt)
print_a_line(2,txt)

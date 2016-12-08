from sys import argv
script,fname=argv
line1="Hello everyone"
line2="have a nice day"
txt=open(fname,'w')
txt.truncate()
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.close()

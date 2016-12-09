A="a b c d e"
a=A.split(' ')
for i in a:
	print i
b=['f','g','h']
print ""
while len(a)!=8:
	#t=b.pop()
	a.append(b.pop())
for i in a:
	print i


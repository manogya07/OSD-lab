fs=open("content.txt")
use={}
words=[]
for i in fs:
	use[i.strip()]=True
	words.append(i)
#print words
for i in range(len(words)):
	st=words[i]
	new=""
	new2=""
	for j in range(0,len(st),2):
		new+=st[j]
	for j in range(1,len(st),2):
		new2+=st[j]
	try:
			if use[new]==True:
				print new,st
			if use[new2]==True:
				print new2,st
	except Exception, e:
		pass
	else:
		pass
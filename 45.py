name=[]
val=[]
visit={}
have=[]

def generate(string,lvl,maxi):
	have.append(string)
	lvl+=1
	go=string[len(string)-1]  #go has last index of parent string
	can=[]                    #list having first index same as go
	for i in range(len(name)):
		st=name[i]
		if st[0]==go and visit[st]=='False':
			can.append(st)
	for i in can:
		visit[i]=True
		generate(i,lvl,maxi)
	maxi=max(maxi,lvl)
	val.append(maxi)
	#print have
	assert(len(have)<=16)
	if len(have)==16:
		print have
	lvl-=1
	have.pop()		

def init():
	for words in name:
		visit.update({words:'False'})
	have=[]

if __name__ == '__main__':
	fp=open("poke.txt")
	for words in fp:
		name.append(words.strip())
		visit.update({words.strip():'False'})
	ans=-1
	for words in name:
		generate(words.strip(),0,0)
		#print "done with " + words
		init()
	print max(val)
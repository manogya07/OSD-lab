fs=file("content.txt")
seq={}
for words in fs:
	freq=[0]*26
	string = words.strip()
	fr=""
	prev=len(seq)
	for i in range(len(string)):
		if ord(string[i])>=97 and ord(string[i])<=123:
			freq[ord(string[i])-97]+=1
		else:
			continue
	for i in range(len(freq)):
		fr+=str(freq[i])
	#seq.update({fr:string})
	try:
		if seq[fr]:
			print string,seq[fr]
	except Exception, e:
		seq.update({fr:string})
		pass
	else:
		pass
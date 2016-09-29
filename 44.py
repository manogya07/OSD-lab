import random
string = ""
for i in range(int(raw_input("Enter length"))):
	x=random.randint(1,100)
	if x%2==0:
		string+='['
	else:
		string+=']'

print string
stk=[]
for i in range(len(string)):
	if string[i]=='[':
		stk.append("1")
	else:
		if len(stk)==0:
			print "Unbalanced String"
			exit(0)
		else:
			stk.pop()
if len(stk)==0:
	print "balanced string"
else:
	print "unbalanced string"

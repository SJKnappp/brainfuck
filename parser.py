
def parser(source):

	open=0

	for char in source:
		if(char=='<'): pass
		elif(char=='>'): pass
		elif(char=='+'): pass
		elif(char=='-'): pass
		elif(char=='.'): pass
		elif(char==','): pass
		elif(char=='['): open+=1
		elif(char==']'):
			if(open>0):
				open-=1

	if (open!=0):
		print(f'there are {open} open brackets')
		quit



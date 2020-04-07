
def parser(source):

	open=0
	pos=0

	for char in source:
		if(char=='<'): 
			pos-=1
			if(pos<0): 
				print('unable to go tp mem address < 0')
				quit

		elif(char=='>'): pos+=1
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



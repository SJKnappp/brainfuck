from parser import *

source = open("source", "r")
output = open("main.asm", "w")

opened=0
loop = []

#intialse file
output.write("section .text\n")
output.write("	global _start\n")
output.write("_start:\n")
output.write("mov ecx, x\n")

data=""
for line in source:
	line=line.strip()
	for char in line:
		if(char=='<'): data+='<'
		elif(char=='>'): data+='>'
		elif(char=='+'): data+='+'
		elif(char=='-'): data+='-'
		elif(char==','): data+=','
		elif(char=='.'): data+='.'
		elif(char=='['): 
			data+='['
			opened+=1
		elif(char==']'): data+=']'

#end file
output.write("mov eax 1\n")
output.write("int 0x80\n")
output.write("section	.data\n")
output.write("global x\n")
output.write("x times 3000 DW 0")

output

parser(data)

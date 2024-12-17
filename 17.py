import numpy as np
#operations
def combo(operand,register):
    if operand<=3:
        return operand
    elif operand<7:
        return register[operand-4]
    else:
        raise ValueError('Illegal combo operand 7')

def adv(operand,register):
    register[0]= int(register[0]//(2**combo(operand,register)))
    return -1,''

def bxl(operand,register):
    register[1]^= operand
    return -1,''

def bst(operand,register):
    register[1]=combo(operand,register)%8
    return -1,''

def jnz(operand,register):
    if register[0]!=0:
        return operand,''
    else:
        return -1,''

def bxc(operand,register):
    register[1]^=register[2]
    return -1,''

def out(operand,register):
    print (f'{combo(operand,register)%8},',end='')
    return -1,str(combo(operand,register)%8)

def bdv(operand,register):
    register[1]= int(register[0]//(2**combo(operand,register)))
    return -1,''

def cdv(operand,register):
    register[2]= int(register[0]//(2**combo(operand,register)))
    return -1,''

instr=(adv,bxl,bst,jnz,bxc,out,bdv,cdv)

register=np.zeros(3,dtype=int)
with open('input_17.txt') as f:
    for line in f:
        if len(line)<2:
            continue
        elif line[9]=='A':
            register[0]=int(line[11:].strip())
        elif line[9]=='B':
            register[1]=int(line[11:].strip())
        elif line[9]=='C':
            register[2]=int(line[11:].strip())
        else:
            code=np.array(list(map(int,line[9:].strip().split(','))))
print (register)
print (len(code),code)
regsave=register.copy()

test = 2385568
while test<=100000000:
    register=regsave.copy()
    register[0]=test
    pointer=0
    outind=0
    correct=1
    #print('Test A',register)
    while pointer<len(code) and correct:
        ret,output=instr[code[pointer]](code[pointer+1],register)
        if len(output)>0:
            #print('Output',output,'Code at ',outind,':',code[outind])
            if code[outind]!=int(output):
                print('Test A failed',test)
                correct=0
            outind+=1
            if outind>len(code):
                correct=0
        if ret==-1:
            pointer +=2
        else:
            pointer = ret  
    if correct:
        if outind==len(code):
            print('Test A successful',test)
            break
        else: 
            print('Test A short',test)
    test+=1

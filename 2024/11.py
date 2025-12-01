


def blink(stone,depth):
    if depth==0:
        #print(stone)
        return 1
    elif stone==0:
        return blink(1,depth-1)
    length=len(str(stone))
    if length%2==0:
        return blink(stone//10**(length//2),depth-1) + blink(stone % 10**(length//2),depth-1)
    else:
        return blink(stone*2024,depth-1)
    
with open('input_11.txt') as f:
    for line in f:
        stones=list(map(int,line.strip().split()))

countstones=0
for stone in stones:
    print('Stone',stone)
    countstones+=blink(stone,75)
print(countstones)
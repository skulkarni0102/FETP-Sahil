input_list = ['F', 'O', 'R', 'M', 'U', 'L', 'A', 'Q', 'S','O','L','U','T','I','O','N','S']

length = len(input_list)
i= int(input("Enter the value"))
cnt=0
itr=1
space = int(i/2)+1
if(i%2 == 0):
    space = int(i/2)+1

for k in reversed(range(0,space)):
    print(" " *k,end="")
    start =cnt%length
    for j in range(itr):
        if(start < length ):
            print(input_list[start],end="")
        else:
            start = 0
            print(input_list[start],end="")
        start += 1
    itr = itr+2
    cnt=cnt+1
    print()
itr = itr-2

if(i%2 != 0):
    space = int(i/2)+1
for k in range(1,space):
    print(" " *k,end="")
    itr = itr-2
    start = cnt%length
    for j in range(itr):
        if(start < length ):
            print(input_list[start],end="")
        else:
            start = 0
            print(input_list[start],end="")
        start += 1
    cnt=cnt+1
    print()


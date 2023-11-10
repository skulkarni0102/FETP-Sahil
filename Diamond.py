def pattern(num):
    input_list = ['F', 'O', 'R', 'M', 'U', 'L', 'A', 'Q', 'S','O','L','U','T','I','O','N','S']
    length = len(input_list)
    STRING=""
    STRING += "Number Of Lines "+ str(num) + "\n"
    i= num
    cnt=0
    itr=1
    space = int(i/2)+1
    if(i%2 == 0):
        space = int(i/2)+1

    for k in reversed(range(0,space)):
        STRING += (" " *k)
        start =cnt%length
        for j in range(itr):
            if(start < length ):
                STRING +=input_list[start]
            else:
                start = 0
                STRING +=input_list[start]
            start += 1
        itr = itr+2
        cnt=cnt+1
        STRING += "\n"
    itr = itr-2

    if(i%2 != 0):
        space = int(i/2)+1
    for k in range(1,space):
        STRING += (" " *k)
        itr = itr-2
        start = cnt%length
        for j in range(itr):
            if(start < length ):
                STRING +=input_list[start]
            else:
                start = 0
                STRING +=input_list[start]
            start += 1
        cnt=cnt+1
        STRING += "\n"

    return STRING
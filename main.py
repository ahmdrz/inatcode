import sys

if (len(sys.argv) != 3) :
    print "Arguments : <statenumber> <output>"
    sys.exit(1)

state = sys.argv[1]
output = sys.argv[2]

if state.isdigit() != True:
    print "Arguments : <statenumber> <output>"
    sys.exit(2)
    
fi = open(output,"w")
    
startno = 100000
endno = 999999
state = int(state)

for i in range(startno,endno):
    result = state * 1000000
    result += i
    temp = result
    control = 0
    position = 2
    while temp != 0:
        control += (temp % 10) * position
        temp /= 10
        position = position + 1
    mod = control % 11
    if mod < 2:
        result = result * 10 + mod
    else:
        result = result * 10 + ( 11 - mod )
    
    output = ('0' * (10-len(str(result)))) + str(result)
    flag = False
    
    for j in range(1,10):
        temp = str(j) * 10
        if (output == temp):
            print output
            flag = True
            break
    
    if (flag == False):
        fi.write(output + "\n")

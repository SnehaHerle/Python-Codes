n = int(raw_input())
k = int(raw_input())
a = int(raw_input())
b = int(raw_input())
flag = 0
output = []
green = a
black = b
if (a ==0  or b ==0) :
    print "NO"
    exit()
elif (a < b and b <= ((a + 1)*k)):
    """print "Yes"""
elif ( a > b and a <= ((b + 1)*k)):
    """print "Yes"""
else:
    print "NO"
    exit()
while(n > 0 ):
    if(a < b):
        if(flag==0):
            for i in range(0,k):
                if( n>0 and black>0):
                    output.append('B')
                    black -= 1
                n -=1
            """print output"""
            flag = 1
        else:
            if (green>0):
                output.append('G')
                green -= 1
                """print output"""
            n -= 1
            flag = 0
    else:
        if(flag==0):
            for i in range(0,k):
                if(n>0 and green>0):
                    output.append('G')
                    green -=1
                n -=1
            """print output"""
            flag = 1
        else:
            if(black>0):
                output.append('B')
                black -= 1
            """print output"""
            n -= 1
            flag = 0
            
if ( green != 0):
    while(green>0):
        output.append('G')
        green -= 1
if ( black != 0):
    while(black>0):
        output.append('B')
        black -= 1

str1 = ''.join(output)
print str1

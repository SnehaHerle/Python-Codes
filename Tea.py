input1 = raw_input()
input2 = raw_input()
input3 = raw_input()
input4 = raw_input()
flag = 0

if (input3 < input2 or input4< input2) :
    print "No"
elif (input3 < input4 and input4 <= ((input3 + 1)*input2)):
    print "Yes"
elif ( input4 < input3 and input3 <= ((input4 + 1)*input2)):
    print "Yes"
while(input1 != 0 ):
    if(input3 < input4):
        if(flag==0):
            for i in range(1,k):
                print "B"
                input1 -= k
                flag = 1
        else :
            print "A"
            input1 -= 1
            flag = 0
    else:
        if(flag==0):
            for i in range(1,k):
                print "A"
                input1 -= k
                flag = 1
        else:
            print "B"
            input1 -= 1
            flag = 0

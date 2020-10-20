#program for printing prime number series upto 1000
x=input('enter starting number ')
y=input('enter end number ')
count=0;
for i in range(x,y):
    if(i>1):
        for j in range(2,i):
            if(i % j ==0):
                break;
        else:
            count=count+1;

            print (i)



print 'count of prime numbers in given range is',count

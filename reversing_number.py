# reversing of given number
x= input("enter any number :");
revnum=0;
while(x>0):
    y=x % 10;
    revnum=revnum*10+y;
    x=x//10;

print 'reverse number is:',revnum





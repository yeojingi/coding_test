a,b=map(int,input().split());L=a*b
while b:a,b=b,a%b
print(a,L//a)
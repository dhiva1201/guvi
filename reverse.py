a=int(input())
sum=0
while(a!=0):
  b=a%10
  sum=sum*10+b
  a=a//10
print(sum)  

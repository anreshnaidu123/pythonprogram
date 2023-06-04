#program 1 to print sum of 1 to n 
n =int(input('enter n value'))
print('entered value',n)
s=0


for i in range(1,n+1):
 sum =s + i
 print(i)
  #sum =0
  #sum =sum +i
print("total sum from 1 to {} is {}".format(n,sum))
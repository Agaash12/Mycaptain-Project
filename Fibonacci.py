def Fib(n):
   if n <= 1:
       return n
   else:
       return (Fib(n - 1) + Fib(n - 2))  
n = int(input("Enter the value: ")) 
for i in range(n):
   print(Fib(i),end = " ")

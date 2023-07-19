#when a function calling itself is called recursion
'''def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''

'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    for i in range(10):
        print(fib(i),end=" ")'''

'''def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,n)
    else:
        return ack(m-1,ack(m,n-1))
print(ack(2,1))'''

#Types of function
'''
<1>head recusion:- in this type of recursion the recusive call is made before processing the function
<2>tail recursion:- in this type of recursion processing of function is done before the recursive call
'''
'''def headprint(n):
    if n==0:
        return 
    else:
        headprint(n-1)
        print(n)
headprint(10)'''

'''def tailprint(n):
    if n==11:
        return
    else:
        print(n)
        tailprint(n+1)
tailprint(1)'''      


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(15))    
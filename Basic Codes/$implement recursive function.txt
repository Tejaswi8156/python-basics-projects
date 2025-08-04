def tri_recursion(n):
    if n<=0: 
	    return 0
    elif n==1:
	    return 1
    else:
	    return n+tri_recursion(n-1)
r=int(input("Enter the range: "))
for n in range (0,r):
    print(tri_recursion(n))
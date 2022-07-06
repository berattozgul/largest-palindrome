def largest_palindrome(digit):
    l=[]
    for i in range(1,10**digit):
        for j in range(1,10**digit):
            n=i*j
            if str(n)==str(n)[::-1]:
                l.append(n)
    return max(l)
print(largest_palindrome(3))
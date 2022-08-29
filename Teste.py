#def fat(n):
   # fat = 1
    #for num in range(2, n + 1):
       # fat *= num
   # return(fat)

def fat(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f






s = 0
n = 0

try:
    while True:
        s += (-1)**n / 2*n+1
        n += 1
        print(s)

except KeyboardInterrupt:
    print('n=',n,',pi=',s)

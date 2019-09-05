n = int(input())

d = dict({
        x: x**2 for x in range(1,n+1)
    })
print(d)
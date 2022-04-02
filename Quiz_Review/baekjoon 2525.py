print('keemsw is cute hamzzi')


a, b = map(int, input().split())
c = int(input())

if b + c < 60:
    print(a, b+c)
elif b + c >= 60:
    hour = (b + c) // 60
    a += hour
    b = (b + c) % 60

    if a > 23:
        a = a - 24
        
print(a, b)


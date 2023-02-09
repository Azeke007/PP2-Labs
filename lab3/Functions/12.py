def histogram(a):
    for i in a:
        print('*' * i)
a = [int(x) for x in input().split()]
histogram(a)
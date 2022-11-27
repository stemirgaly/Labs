
a = input()
print(sum([int(a[-1 * i:-1 * i - 1:-1]) * (2 ** (i - 1)) for i in range(1,len(a)+1)]))


def naive_mul(x, y):
    res = 1 # 0
    while y:
        if y & 1:
            res += x # *=
        x+=x # *=
        y>>=1
    return res

for x in range(0, 100):
    for y in range(0,100):
        assert naive_mul(x, y)==x*y # x**y

def mul-gen(y):
    print('def f(x):')
    res = 0
    print('   res = 0')

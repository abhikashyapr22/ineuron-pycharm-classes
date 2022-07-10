from collections import defaultdict

def find_lcm(*n):
    """since lcm is a multiple of every number of the
    list so making use of this property"""
    i = 0
    #print(n)
    d = defaultdict(int)
    for i in range(len(n)):
        d[i] = n[i]
    #print(d)
    lt = list(d.values())
    print(lt)
    flag = True
    while flag:
        for i in range(1,len(lt)):
            if lt[i] == lt[i-1]:
                continue
            else:
                el = lt.pop(lt.index(min(lt)))
                lt.insert()

        flag = False

ans = find_lcm(3,4,6)
print(ans)
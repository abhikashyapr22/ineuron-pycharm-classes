def find_lcm(a,b):
    lcm = a*b
    for i in [2,3,5,7,11,13,17,19,23,29]:
        print(i)
        while a%i == 0 and b%i == 0 and lcm:
            lcm /= i
 
    return lcm

def find_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

#print(find_hcf(50,13))

print((find_lcm(12,15)))
'''
Basic Matrix Operation [reading and displaying]
'''
def fun():
    a=[]
    print("Type 12 elements:")
    for i in range(3):
        b=[]
        for j in range(4):
            b.append(int(input()))
        a.append(b)
    print(a)
    for i in range(3):
        for j  in range(4):
            print(a[i][j], end=' ')
        print()
fun()
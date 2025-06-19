'''
WAP to create an nxn tri-diagonal matrix
'''
def main():
    a = []  #declaring an empty matrix
    n = int(input("Enter width/height of nxn matrix"))
    for i in range(n):
        b = [] # Taking a temporary empty list
        for j in range(n):
            if i == j or i+1 == j or i == j+1:
                b.append(1)
            else:
                b.append(0)
        a.append(b)
    print("Unit matrix is")
    for n in a:
        for m in n:
            print(m, end=' ')
        print()
if __name__ == '__main__':
    main()
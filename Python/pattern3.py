"""

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5  


"""
def pattern()->None:
    for i in range(1, 6):
        for j in range(1, 6):
            print(i, end=' ') # here we are printing value of i
        print()

if __name__ =='__main__':
    pattern()

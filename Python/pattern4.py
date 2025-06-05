"""

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5   


"""
def pattern()->None:
    for i in range(1, 6):
        for j in range(1, 6):
            print(j, end=' ') # Now we are printing value of i
        print()

if __name__ =='__main__':
    pattern()

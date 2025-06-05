"""

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1    


"""
def pattern()->None:
    for i in range(1, 6):
        for j in range(1, 6):
            if i==j:
                print('1', end = ' ')
            else:
                print('0', end = ' ')
        print()

if __name__ =='__main__':
    pattern()

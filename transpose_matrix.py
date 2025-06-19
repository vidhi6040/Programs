'''
WAP to read elements of an nxn matrix and then transpose the same
'''
def main():
    matrix = []
    n = int(input('Enter value of n'))
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(int(input()))
        matrix.append(row_list)
    print("Input Matrrix is")
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print("Input Matrrix is")
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

if __name__ == '__main__':
    main()
            
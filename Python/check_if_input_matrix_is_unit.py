'''
WAP to check if the input 3x3 matrix is an unit matrix
'''

def main():
    input_matrix = []
    print('Type 9 elements of a 3x3 matrix')
    for i in range(3):
        temp_list = []
        for j in range(3):
            temp_list.append(int(input()))
        input_matrix.append(temp_list)
    print("Input Matrix is")
    for list in input_matrix:
        for element in list:
            print(element, end=' ')
        print()
    flag = True
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[1])):
            if i == j and input_matrix[i][j] != 1:
                flag = False
                break
            if i != j and input_matrix[i][j] != 0:
                flag = False
                break
    print('Unit Matrrix') if flag else print('Not Unit Matrrix')

if __name__ == '__main__':
    main()

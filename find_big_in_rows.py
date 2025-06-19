'''
Find out biggest element in each row in an initialized jagged matrix
'''
def main():
    list_of_list = [[3, 4, 7, 9, 3], [5, 1, 3], [4, 2,7, 1]]
    print('The initialized jagged matrix is')
    for list in list_of_list:
        for element in list:
            print(element, end=' ')
        print()
    row_number = 0
    for list in list_of_list:
        row_number = row_number + 1
        big_element = list[0]
        for element in list:
            if element > big_element:
                big_element = element
        print(f'The biggest element in {row_number} is {big_element}')

if __name__ == '__main__':
    main()
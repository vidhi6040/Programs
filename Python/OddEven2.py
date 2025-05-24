def odd_even(n):

    print("Even") if (n%2) == 0 else print ("Odd")
    """
    if (n%2)==0:
        print("Even Number")
    else:
        print("Odd number")
    """
def main():
    a = int(input("Enter an integer: "))
    odd_even(a)

if __name__ == "__main__":
    main()
            

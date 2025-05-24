def big_of_two(a, b):
    # if we want to print here itself
    #print(f"{a} is big") if a > b else print(f"{b} is big")
    return a if a > b else b # if we want to return
    
def main():

    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    print(f"{big_of_two(x,y)} is big")

if __name__ == "__main__":
    main()

def day_name(n: int) -> None:
    match n:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
def main():
    day_name(4)

if __name__ == "__main__":
    main()

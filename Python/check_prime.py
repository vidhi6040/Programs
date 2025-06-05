def is_prime(n: int) -> None:
    for i in range(2, n//2+1):
        if n%i == 0:
            print(f'{n} is not prime')
            break
    else:
        print(f'{n} is prime')
def main():
    x = int(input("Enter an integer: "))
    is_prime(x)

if __name__ == "__main__":
    main()

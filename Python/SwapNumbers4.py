def swap():
    a = 10
    b = 20
    print(f"a is {a} and b is {b}")
    a, b = b, a

    print(f"a is {a} and b is {b}")

if __name__ == "__main__":
    swap()

def swap():
    a = 10
    b = 20
    print(f"a is {a} and b is {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"a is {a} and b is {b}")

if __name__ == "__main__":
    swap()

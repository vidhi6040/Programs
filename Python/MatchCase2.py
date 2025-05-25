def day_name(n: int) -> str:
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wenesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        }.get(n);
def main():
    print(f"{day_name(4)}")

if __name__ == "__main__":
    main()

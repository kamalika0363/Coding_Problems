def last_one_standing(s: str, k: int) -> str:
    extended_s = s * k

    while len(extended_s) > 1:
        extended_s = extended_s[1::2]

        if len(extended_s) > 1:
            extended_s = extended_s[:-1:2]

    return extended_s


def main():
    s = input("Enter the string: ")
    k = int(input("Enter the value of k: "))

    result = last_one_standing(s, k)
    print(f"The last one standing is: {result}")


if __name__ == "__main__":
    main()

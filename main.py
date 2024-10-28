

def main():
    user_input = input("Hey chat, type 1 if we're computing the fibonacci, 2 for factorials\n> ")
    if user_input == "1":
        print(fibonacci(10))
    elif user_input == "2":
        print(factorial(10))
    else:
        print("Bruh")


def fibonacci(n: int) -> int:
    pass


def factorial(n: int) -> int:
    pass


if __name__ == "__main__":
    main()


# These are some tricky things about Exceptions


def main():
    number = get_number()
    print(f"The number is {number}")


def get_number():
    while True:
        try:
            return int(input("Enter the number : "))
        except ValueError:
            # print("You have given something else.....")
            pass
        
main()

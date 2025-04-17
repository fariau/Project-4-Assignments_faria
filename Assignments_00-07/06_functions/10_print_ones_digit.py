def print_ones_digit(num):
    # Find the ones digit using modulo operator
    print("The ones digit is", num % 10)

def main():
    # Get input from the user
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()

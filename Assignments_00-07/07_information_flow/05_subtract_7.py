def subtract_seven(num):
    return num - 7  # Subtracts 7 from the given number

def main():
    # Get user input
    number = int(input("Enter a number: ")) 
    # Call the helper function 
    result = subtract_seven(number)  
    # Print the result
    print("Result after subtracting 7:", result)  

if __name__ == '__main__':
    main()
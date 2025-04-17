def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")
    
    # Call the num_in_stock function to get the stock count for that fruit
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print the appropriate message
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    # Hardcoded inventory for demonstration
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # Return 0 if the fruit is not in stock
        return 0

# Ensure the program runs when executed
if __name__ == '__main__':
    main()

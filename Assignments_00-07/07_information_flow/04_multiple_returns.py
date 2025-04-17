def get_user_info():
    # Ask the user for their first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return all the data as a tuple
    return first_name, last_name, email_address

def main():
    # Call the function to get user data and store it
    user_data = get_user_info()
    
    # Print the collected data
    print("Received the following user data:", user_data)

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()

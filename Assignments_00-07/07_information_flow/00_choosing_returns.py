ADULT_AGE = 18  # U.S. legal age for adulthood

def is_adult(age: int):
    # Directly return the comparison result
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))  # Convert input to integer
    print(is_adult(age))  # Print whether the person is an adult or not

if __name__ == "__main__":
    main()

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0
    for fruit in fruits:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * fruits[fruit]

    print("Your total is $" + str(total_cost))


if __name__ == '__main__':
    main()

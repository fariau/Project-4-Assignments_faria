C: int = 299792458  # The speed of light in m/s

def main():
    while True:
        try:
            mass_in_kg: float = float(input("Enter kilos of mass: "))
            energy_in_joules: float = mass_in_kg * (C ** 2)
            print("e = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(str(energy_in_joules) + " joules of energy!\n")
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == '__main__':
    main()

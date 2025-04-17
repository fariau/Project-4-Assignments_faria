SENTANCE_START : str = "Panaversity is fun. I learned to program and used python to make my "

def main():
    adjective : str = input("Enter an adjective and press enter:")
    noun : str = input("Enter an noun and press enter:")
    verb : str = input("Enter an verb and press enter:")
    
    print(SENTANCE_START + adjective + " " + noun + " " + verb + ".")
    
if __name__ == "__main__" :
    main()
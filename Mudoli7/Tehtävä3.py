
def main():
    airports = {}

    while True:
        action = input("\nChoose an action: (1) Enter new airport, (2) Search airport, (3) Quit: ")

        if action == '1':
            icao = input("Enter ICAO code: ").upper()
            name = input("Enter airport name: ")
            airports[icao] = name
            print(f"Added: {icao} - {name}")

        elif action == '2':
            icao = input("Enter ICAO code to search: ").upper()
            print(f"Airport: {airports.get(icao, 'Not found')}")

        elif action == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
main()
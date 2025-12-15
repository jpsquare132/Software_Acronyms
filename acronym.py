def find_acronym():
    try: 
        lookup = input("What software acronym would you like to look up?\n").upper()

        found = False
        with open('input.txt', 'r') as file:
            for line in file:
                if lookup in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return
    if not found:
        print('The acronym does not exist')
        
def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input('What is the definition?\n)')
    with open('input.txt', 'a') as file:
        file.write(f'{acronym} - {definition}\n')

def main():
    choice = input("Do you want to find(F) or add(A) an acronym?\n")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
main()
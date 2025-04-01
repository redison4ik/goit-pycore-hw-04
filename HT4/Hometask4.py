def parse_input(user_input):  #обробка команд користувача
    cmd, *args = user_input.split() # розділення команди та аргументів
    cmd = cmd.strip().lower() # нижній регістр
    return cmd, *args 

def add_contact(args, contacts): # додавання контакту
    name, phone = args 
    contacts[name] = phone # словник
    return "Contact added."

def change_contact(args, contacts): # зміна контакту
    name, phone = args
    if name in contacts: # якщо контакт існує
        contacts[name] = phone # зміна телефону
        return "Contact changed."
    else:
        return "Contact not found."

def show_contact(args, contacts): # показати контакт
    name = args[0] # перший аргумент
    if name in contacts: # якщо контакт існує
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."
    
def show_all(contacts): # показати всі контакти
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {} # створення словника
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ") # введення команди
        command, *args = parse_input(user_input) # обробка команди

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all": 
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__": # точка входу
    main()
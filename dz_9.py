import re

user_contacts = {} 

def user_help ():
   return """
          Phone book commands:
          1. hello
          2. add 'Name' 'phone number" (Igor +380989709609')
          3. change 'Name' phone number (Igor +380989709609')
          4. phone 'Name'
          5. show all
          6. good bye
          7. close
          8.exit
          """
 
# Decorator input errors
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return f"This contact {' '.join(args)} doesn't exist in the phone book"
        except ValueError:
            return "The entered name and phone number do not match the given parameter. For help, type 'help'"
        except IndexError:
            return "Type all params for command. For help, type 'help'"

    return wrapper

# Greetings
@input_error
def user_hello(*args):
    return "How can I help you?"

# Add
@input_error
def user_add(*args):
    name = args[0]
    phone = args[1]
    
    if not re.match(r"^\+[\d]{12}$", phone):
        raise ValueError
    
    if len(user_contacts) == 0:
        user_contacts[name] = phone 
        return f"{name} : {phone} has been added to the phone book"
    else:    
        if name in user_contacts:
            return f"User {name} is already in the phone book."
        elif phone in user_contacts.values():
            # Помогите разобраться с написанием строки, не получается. Параметр name_user
            # name_user for name_user in user_contacts if phone in user_contacts.value()
            return f"This phone {phone} is in the book. Pinned to user name_user."
        else:
            user_contacts[name] = phone 
            return f"{name} : {phone} has been added to the phone book"
   
# Change
@input_error
def user_change(*args):
    name = args[0]
    phone = args[1]

    if not re.match(r"^\+[\d]{12}$", phone):
        raise ValueError
    
    if name not in user_contacts:
        return f"User {name} is not in the phone book."
    else:
        user_contacts[name] = phone
        return f"The phone {phone} for {name} has been updated"
    
# Contact phone number
@input_error
def user_phone(*args):
    name = args[0]
    return f"The phone number for {name} is {user_contacts[name]}"

# Show all
@input_error
def user_show_all(*args):
    
    all = ""
    
    if len(user_contacts) == 0:
        return "Phone book is empty"
    else:
        for name, phone in user_contacts.items():
            all += f"{name}: {phone}\n"
        return all
    
# Exit
def user_exit(*args): 
    return "Good bye!\n"

COMMANDS = {
    'hello': user_hello,
    'add': user_add,
    'change': user_change,
    'phone': user_phone,
    'show all': user_show_all,
    'good bye': user_exit,
    'close': user_exit,
    'exit': user_exit,
    'help': user_help,
}
 
# Command processing
def command_handler(user_input: str):
    for cmd in COMMANDS:
        if user_input.startswith(cmd):
            return COMMANDS[cmd], user_input.replace(cmd, '').strip().split()
    return None, []

def main():
    
    print(user_help())

    while True:
        user_input = input("Enter a command: ")
        command, data = command_handler(user_input)

        if command == user_exit:
            break

        if not command:
            print("Command is not supported. Try again.")
            continue
        
        print(command(*data))


if __name__ == "__main__":
    main()

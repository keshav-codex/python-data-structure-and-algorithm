# take user choice and perform operations
'''
1. View list
2. Add element
3. Insert element
4. Update element
5. Remove element
6. Pop element
7. Clear list
8. Search element
9. Count element
10. Sort list
11. Reverse list
12. Exit
'''

def choice_operation(operation_list, choice):

    match choice:

        case '1':
            # view list => print list
            print(operation_list)
            return True

        case '2':
            # add element
            user_input = input("input value to add : ")
            operation_list.append(user_input)
            print(f"List after 'Add element operation' : {operation_list}")
            return True

        case '3':
            # Insert operation
            index = input("Input a positive number : ")
            if not index.isdigit():
                print(f"Enter positive digit")
            else:
                user_input = input("input value to add : ")
                operation_list.insert(int(index), user_input)
                print(f"List after 'Insert element operation' : {operation_list}")

            return True

        case '4':
            # Update element
            index = input("Input index to update : ")
            if not index.isdigit() or int(index) >= len(operation_list):
                print(f"Enter a valid index")
            else:
                user_input = input("input new value : ")
                operation_list[int(index)] = user_input
                print(f"List after 'Update element operation' : {operation_list}")

            return True

        case '5':
            # Remove element
            user_input = input("input value to remove : ")
            if user_input not in operation_list:
                print(f"Value not found in list")
            else:
                operation_list.remove(user_input)
                print(f"List after 'Remove element operation' : {operation_list}")

            return True

        case '6':
            # Pop element
            index = input("Input index to pop (leave blank for last element) : ")
            if index == '':
                if not operation_list: # empty list is falsy in python
                    print(f"List is empty")
                else:
                    popped = operation_list.pop()
                    print(f"Popped value : {popped}")
                    print(f"List after 'Pop element operation' : {operation_list}")
            elif not index.isdigit() or int(index) >= len(operation_list):
                print(f"Enter a valid index")
            else:
                popped = operation_list.pop(int(index))
                print(f"Popped value : {popped}")
                print(f"List after 'Pop element operation' : {operation_list}")

            return True

        case '7':
            # Clear list
            operation_list.clear()
            print(f"List after 'Clear list operation' : {operation_list}")
            return True

        case '8':
            # Search element
            user_input = input("input value to search : ")
            if user_input in operation_list:
                print(f"'{user_input}' found at index {operation_list.index(user_input)}")
            else:
                print(f"'{user_input}' not found in list")

            return True

        case '9':
            # Count element
            user_input = input("input value to count : ")
            print(f"'{user_input}' appears {operation_list.count(user_input)} time(s)")
            return True

        case '10':
            # Sort list
            try:
                operation_list.sort()
                print(f"List after 'Sort list operation' : {operation_list}")
            except TypeError:
                print(f"Cannot sort list with mixed types")

            return True

        case '11':
            # Reverse list
            operation_list.reverse()
            print(f"List after 'Reverse list operation' : {operation_list}")
            return True

        case '12':
            # Exit
            print("Exiting...")
            return False

        case _:
            print("Invalid choice, please try again")
            return True


def main():
    operation_list = []
    operation_mode = True
    while operation_mode:
        print(f"""
        Enter code for operation
        ************************
        1. View list
        2. Add element
        3. Insert element
        4. Update element
        5. Remove element
        6. Pop element
        7. Clear list
        8. Search element
        9. Count element
        10. Sort list
        11. Reverse list
        12. Exit
        """)

        choice = input().strip()
        operation_mode = choice_operation(operation_list, choice)

if __name__ == "__main__":
    main()
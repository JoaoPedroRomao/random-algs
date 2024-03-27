import os
os.system('cls' if os.name == 'nt' else 'clear')

lst = []

while True:
    i = input('What do you want to do? ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if i == 'exit':
        break
    elif i == 'help':
        print('This program allows you to manipulate lists according to your input!')
        print('Here are the following commands you can use:')
        print('list length: length')  # len
        print('list objects in a line: info')  # print list
        print('object in index on the list: index')  # search by index
        print('last object added: last')  # negative index
        print('objects in index range: range index')  # range index
        print('all objects until specified index: until')  # (:x)
        print('all objects after index: after')  # (x:)
        print('know if there is a specific string in the list by name: string')  # if x in lst:
        print('know if there is a specific integer in the list by name: integer')
        print('know if there is a specific float value in the list by name: float')
        print('change a specific object in the list: change')  # lst[x] = new object
        print('insert a new object in the list at index: insert')  # lst.insert(index,'oject')
        print('append new strings to the list: append strings')
        print('append new integers to the list: append integer')  # lst.append('object')
        print('append new floats to the list: append float')
        print('remove a specific string in the list: remove string')  # lst.remove('object')
        print('remove a specific integer in the list: remove integer')  # lst.remove('object')
        print('remove a specific float in the list: remove float')  # lst.remove('object')
        print('remove a specific object from the list by index: pop or del')  # lst.pop(index) #del lst[index]
        print('remove all objects in the list: clear')  # lst.clear()
        print('list objects in the list in a column: list')  # [print(x) for x in lst]
        print('to exit the program type: exit')
        print('to read again type: help')
    elif i == 'length':
        print('The length of the list is:', len(lst))
    elif i == 'info':
        print('The list contains:', lst)
    elif i == 'index':
        while True:
            var = input('Which index do you want to search? ')
            if var.isdigit():
                var = int(var)
                if 0 <= var < len(lst):
                    print('Object at index', var, 'is:', lst[var])
                    break
                else:
                    print('Index out of range, please try again.')
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'last':
        if lst:
            print('The last object added was:', lst[-1])
        else:
            print('The list is empty.')
    elif i == 'range index':
        while True:
            var_1 = input('From what index do you want to start? ')
            var_2 = input('Until which index do you want to go? ')
            if var_1.isdigit() and var_2.isdigit():
                var_1 = int(var_1)
                var_2 = int(var_2)
                if 0 <= var_1 < len(lst) and 0 <= var_2 < len(lst):
                    if var_2 <= var_1:
                        print('Indexes out of order or equal, please try again.')
                    else:
                        print('Objects from index', var_1, 'to', var_2, 'are:', lst[var_1:var_2])
                        break
                else:
                    print('Indexes out of range, please try again.')
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'after':
        while True:
            index = input('From which index do you want to see the objects? ')
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(lst):
                    print('Objects after index', index, 'are:', lst[index:])
                    break
                else:
                    print('Index out of range, please try again.') 
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'until':
        while True:
            var = input('Until which index do you want to see the objects? ')
            if var.isdigit():
                var = int(var)
                if 0 <= var < len(lst):
                    print('Objects until index', var, 'are:', lst[:var])
                    break
                else:
                    print('Index out of range, please try again.') 
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'string':
        while True:
            var = input('Enter the string you are looking for: ')
            if var in lst:
                print('The string', var, 'is in the list at index:', lst.index(var))
                break
            else:
                print('The string is not in the list or is not a string value, please try again.')
        continue
    elif i == 'integer':
        while True:
            var = input('Enter the integer value you are looking for: ')
            if var.isdigit():
                var = int(var)
                if var in lst:
                    print('The integer', var, 'is in the list at index:', lst.index(var))
                    break
                else:
                    print('The integer is not in the list or is not an integer value, please try again.')
            else:
                print('Invalid input. Please enter a valid integer value.')
        continue
    elif i == 'float':
        while True:
            var = input('Enter the float value you are looking for: ')
            try:
                var = float(var)
                if var in lst:
                    print('The float', var, 'is in the list at index:', lst.index(var))
                    break
                else:
                    print('The float is not in the list or is not a float value, please try again.')
            except ValueError:
                print('Invalid input. Please enter a valid float value.')
        continue
    elif i == 'change':
        while True:
            var = input('Which index do you want to replace? ')
            if var.isdigit():
                var = int(var)
                if 0 <= var < len(lst):
                    change = input('Enter the new value: ')
                    lst[var] = change
                    print('List after replacement:', lst)
                    break
                else:
                    print('Index out of range, please try again.')
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'insert':
        while True:
            print('Note: Objects after the specified index will be shifted by one position.')
            index = input('Enter the index where you want to insert the object: ')
            if index.isdigit():
                index = int(index)
                if 0 <= index <= len(lst):
                    new_object = input('Enter the new object: ')
                    lst.insert(index, new_object)
                    print('List after insertion:', lst)
                    break
                else:
                    print('Index out of range, please try again.')
            else:
                print('Invalid index. Please enter a valid number.')
        continue
    elif i == 'append strings':
        while True:
            count = input('How many strings do you want to insert? ')
            if count.isdigit():
                count = int(count)
                if count > 0:
                    for _ in range(count):
                        string_input = input('Enter the string: ')
                        lst.append(string_input)
                    print('List after appending strings:', lst)
                    break
                else:
                    print('Please enter a number greater than 0.')
            else:
                print('Invalid input. Please enter a valid number.')
        continue
    elif i == 'append integer':
        while True:
            count = input('How many integers do you want to insert? ')
            if count.isdigit():
                count = int(count)
                if count > 0:
                    for _ in range(count):
                        number_input = input('Enter the integer: ')
                        if number_input.isdigit():
                            lst.append(int(number_input))
                        else:
                            print('Input discarded. Please type integers when using this command!')
                    print('List after appending integers:', lst)
                    break
                else:
                    print('Please enter a number greater than 0.')
            else:
                print('Invalid input. Please enter a valid number.')
        continue
    elif i == 'append float':
        while True:
            count = input('How many floats do you want to insert? ')
            if count.isdigit():
                count = int(count)
                if count > 0:
                    for _ in range(count):
                        while True:
                            float_input = input('Enter the float: ')
                            try:
                                float_value = float(float_input)
                                lst.append(float_value)
                                break
                            except ValueError:
                                print('Input discarded. Please type floats when using this command!')
                    print('List after appending floats:', lst)
                    break
                else:
                    print('Please enter a number greater than 0.')
            else:
                print('Invalid input. Please enter a valid number.')
        continue
    elif i == 'remove string':
        while True:
            string_to_remove = input('Enter the string you want to remove: ')
            if string_to_remove in lst:
                lst.remove(string_to_remove)
                print('String removed. Updated list:', lst)
                break
            else:
                print('The string is not in the list or is not a string value. Please try again.')
        continue
    elif i == 'remove integer':
        while True:
            integer_to_remove = input('Enter the integer you want to remove: ')
            if integer_to_remove.isdigit():
                integer_to_remove = int(integer_to_remove)
                if integer_to_remove in lst:
                    lst.remove(integer_to_remove)
                    print('Integer removed. Updated list:', lst)
                    break
                else:
                    print('The integer is not in the list or is not an integer value. Please try again.')
            else:
                print('Invalid input. Please enter a valid integer.')
        continue
    elif i == 'remove float':
        while True:
            float_to_remove = input('Enter the float you want to remove: ')
            try:
                float_to_remove = float(float_to_remove)
                if float_to_remove in lst:
                    lst.remove(float_to_remove)
                    print('Float removed. Updated list:', lst)
                    break
                else:
                    print('The float is not in the list or is not a float value. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a valid float.')
        continue
    elif i == 'pop':
        while True:
            index_to_remove = input('Enter the index you want to remove: ')
            if index_to_remove.isdigit():
                index_to_remove = int(index_to_remove)
                if 0 <= index_to_remove < len(lst):
                    popped_item = lst.pop(index_to_remove)
                    print('Item at index', index_to_remove, 'removed:', popped_item)
                    print('Updated list:', lst)
                    break
                else:
                    print('Index out of range, please try again.')
            else:
                print('Invalid input. Please enter a valid index.')
        continue
    elif i == 'del':
        while True:
            index_to_delete = input('Enter the index you want to delete: ')
            if index_to_delete.isdigit():
                index_to_delete = int(index_to_delete)
                if 0 <= index_to_delete < len(lst):
                    del lst[index_to_delete]
                    print('Item at index', index_to_delete, 'deleted.')
                    print('Updated list:', lst)
                    break
                else:
                    print('Index out of range, please try again.')
            else:
                print('Invalid input. Please enter a valid index.')
        continue
    elif i == 'clear':
        while True:
            confirmation = input('Are you sure you want to clear the list? (y/n): ').lower()
            if confirmation == 'y':
                lst.clear()
                print('List cleared.')
                break
            elif confirmation == 'n':
                print('Clear operation canceled.')
                break
            else:
                print('Invalid input. Please enter either "y" or "n".')
        continue
    elif i == 'list':
        for item in lst:
            print(item)
        continue
    else:
        print('Invalid command. Type "help" for available commands.')
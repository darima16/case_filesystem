"""Case-study#2
Developers:
Rashidova A. (61%), Zhambaeva D. (59%), Ganbat S. (56%)
"""


import os
import os.path
from rulocal import *

counter = 0
bytes_ = 0


def accept_command():
    """ A function that requests the command number. """
    try:
        command = int(input(COMMAND_NUMBER))
        if command in range(1, 8):
            return command
        else:
            return
    except:
        return


def run_command(command):
    """ A function that determines by the command number what function should be performed. """
    if command is None:
        print(NOT_FOUND_ERROR)
        return
    elif command == 1:
        print(directory())
    elif command == 2:
        move_up()
    elif command == 3:
        subdir = input(INPUT_SUBDIR)
        move_down(subdir)
    elif command == 4:
        path = os.getcwd()
        print(count_files(path))
        os.chdir(path)
    elif command == 5:
        path = os.getcwd()
        print(count_bytes(path))
        os.chdir(path)
    elif command == 6:
        target = input(INPUT_FILE)
        path = os.getcwd()
        result = find_files(target, path)
        if result is True:
            print(CORRECT_FILE)


def directory():
    """ A function that shows whole catalogue. """
    return os.listdir(os.getcwd())


def move_up():
    """ A function that makes the parent directory current directory. """
    my_path = os.getcwd()
    catalogue = my_path.rfind('\\')
    return os.chdir(my_path[:catalogue])


def move_down(subdir):
    """ A function that makes the directory in the "subdir" current if the name specified correctly,
     otherwise displays an error message. """
    try:
        cur_dir = os.getcwd()
        new_dir = os.path.join(cur_dir, subdir)
        return os.chdir(new_dir)
    except FileNotFoundError:
        print(INPUT_ERROR)


def down(subdir):
    """ An additional function to go down. """
    try:
        cur_dir = os.getcwd()
        new_dir = os.path.join(cur_dir, subdir)
        return os.chdir(new_dir)
    except FileNotFoundError:
        return


def count_files(path):
    """ A recursive function that counts the number of files in the specified  directory "path". """
    global counter
    for file in directory():
        if os.path.isfile(path + '\\' + file):
            counter += 1
        if os.path.isdir(path + '\\' + file):
            down(file)
            count_files(path + '\\' + file)
    return counter


def count_bytes(path):
    """ A recursive function that counts the total amount of all files in the specified "path" directory in bytes. """
    global bytes_
    for file in directory():
        if os.path.isfile(path + '\\' + file):
            bytes_ += os.path.getsize(path + '\\' + file)
        if os.path.isdir(path + '\\' + file):
            down(file)
            count_bytes(path + '\\' + file)
    return bytes_


def find_files(target, path):
    """ A recursive function that generates a list of paths to files whose name contains the "target". """
    if target in directory():
        return True
    for file in directory():
        if os.path.isdir(path + '\\' + file):
            down(file)
            find_files(os.getcwd(), target)


def main():
    """ The main function. """
    while True:
        print(os.getcwd())
        print(MENU)
        command = accept_command()
        if command == 7:
            break
        run_command(command)
    print(END)


if __name__ == '__main__':
    main()

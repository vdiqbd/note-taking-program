# ----------------------------------------------------------------------------------------------------
import os
# ----------------------------------------------------------------------------------------------------
filename = input('Enter the name of the file: ')
mode = 'r'
# ----------------------------------------------------------------------------------------------------
def ifNotExists(f, m):
    with open(f, m) as file:
        print('File has been created.')
        text = input('Enter the text you want to write to the file: ')
        file.write(text)
# ----------------------------------------------------------------------------------------------------
def read(f, m):
    with open(f, m) as file:
        lines = file.read()
        print(lines)
# ----------------------------------------------------------------------------------------------------
def delete(f, m):
    print('File has been deleted and a new one has been created.')
    response = input('Do you have anything to write to the new file(Y/N): ').upper()
    if response == 'Y':
        text = input('Enter the text you want to write to the file: ')
        with open(f, m) as file:
            file.write(text)
    else:
        quit()
# ----------------------------------------------------------------------------------------------------
def append(f, m):
    text = input('Enter the text you would like to append to the file: ')
    with open(f, m) as file:
        file.write(f'\n{text}')
# ----------------------------------------------------------------------------------------------------
if os.path.exists(filename):
    res = input('Do you want to read(r), delete and start over(d) or append(a) to the file: ').lower()
    if res == 'r':
        read(filename, mode)
    elif res == 'd':
        mode = 'w'
        delete(filename, mode)
    elif res == 'a':
        mode = 'a'
        append(filename, mode)
else:
    mode = 'w'
    ifNotExists(filename, mode)
# ----------------------------------------------------------------------------------------------------

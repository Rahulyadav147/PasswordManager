import getpass

def store_info():
    info_file = open('info.txt', 'a')
    website = input('Enter website name: ')
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ') #getpass default value change
    info_file.write(f'{website},{username},{password}\n')
    info_file.close()
    print('Information stored successfully!')

def retrieve_info():
    info_file = open('info.txt', 'r')
    website = input('Enter website name: ')
    found = False
    for line in info_file:
        if website in line:
            values = line.strip().split(',', 2)  # split on first two commas only
            if len(values) == 3:
                website, username, password = values
                print(f'Username: {username}\nPassword: {password}')
                found = True
            else:
                print(f'Error: could not retrieve information for {website}')
    info_file.close()
    if not found:
        print(f'Error: no information found for {website}')


while True:
    action = input('Do you want to store or retrieve information? ')
    if action.lower() == 'store':
        store_info()
    elif action.lower() == 'retrieve':
        retrieve_info()
    else:
        print('Invalid action. Please try again.')
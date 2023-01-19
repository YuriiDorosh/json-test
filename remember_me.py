import json


def get_stored_username():
    # Get a name
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None


def greet_user():
    # Greet user
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = input('What is your name? ')
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f'We`ll remember you when you come back, {username}!')


greet_user()

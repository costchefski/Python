import random

possible_usernames = ['admin', 'alice', 'jaybyrd', 'moomin', 'bossman']

actual_username = random.choice(possible_usernames)

if actual_username == 'admin':
        print(f"Hello, {actual_username}. Press CTRL+S for status report.")
else:
        print(f"Hello, {actual_username}. Good to see you log in again.")

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed_users.
# Move each verified user into the list of confirmed_users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed_users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

from random import *

age = randint(1, 100)    # Pick a random number between 1 and 100.

if age < 2:
    print("You're still a baby!")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You're a kid, kiddo.")
elif age < 20:
    print("You're a teenager and you probably hate this script.")
elif age < 65:
    print("You are an adult. Can I borrow $50?")
elif age >= 65:
    print("You are an elderly person.")

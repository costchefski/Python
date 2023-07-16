guests = ['alice', 'bob', 'gwendoline', 'ashley']

for guest in guests:
    print(f"Hi, {guest.title()}, will you come to my party?")

rsvp_no = 'alice'
print(f"\nUnfortunately, {rsvp_no.title()} can't make it.")

guests.remove(rsvp_no)
guests.insert (-1, 'denice')

for guest in guests:
    print(f"\nHi, {guest.title()}, will you come to my party still?")

print("\n Oh, hey, a bigger dinner table!\n")

guests.insert(0, 'sebastien')
guests.insert(3, 'hitomi')
guests.append('ethan')

for guest in guests:
    print(f"Hey, {guest.title()}, will you come to my Extended dinner party?")

print("\nOkay, sorry, only two of you are coming.\n")

cut_guest = guests.pop(0)
print(f"Sorry, {cut_guest.title()}, maybe next time?")

cut_guest = guests.pop(-1)
print(f"Sorry, {cut_guest.title()}, maybe next time?")

cut_guest = guests.pop(1)
print(f"Sorry, {cut_guest.title()}, maybe next time?")

cut_guest = guests.pop(3)
print(f"Sorry, {cut_guest.title()}, maybe next time?")

cut_guest = guests.pop(2)
print(f"Sorry, {cut_guest.title()}, maybe next time?")

for guest in guests:
    print(f"Hey, {guest.title()}, definitely still on!")

del guests[0]
del guests[-1]
print(guests)

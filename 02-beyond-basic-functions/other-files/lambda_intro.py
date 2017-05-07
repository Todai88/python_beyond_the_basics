#This is an intro to lambda functions.

names = ["Bethany Ditzel", "Joakim Bajoul", "Bork Borkins", "Fredrik Edlund"]

print(sorted(names, key=lambda NAMES: NAMES.split()[-1]))
print(sorted(names, key=lambda NAMES: NAMES.split()[0]))
print(sorted(names, key=lambda NAMES: NAMES.split()[0], reverse=True))

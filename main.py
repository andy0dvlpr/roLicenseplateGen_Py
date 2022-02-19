import roplategen

print("How many license plates to generate?")
print("Press [ENTER] for default (1).")
choice = input()
if choice == "":
    choice = 1

for i in range(int(choice)):
    roplategen.roplategen()
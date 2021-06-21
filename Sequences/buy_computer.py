availble_parts = ["Computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "HDMI Cable",
                  "DVD Drive"]
#valid_choices = [str(i) for i in range(1, len(availble_parts)+1)]
valid_choices = []
for i in range (1, len(availble_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "_"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) -1
        chosen_part = availble_parts[index]
        if chosen_part in computer_parts:
            # its already in the list, remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Addinig {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains {}".format(computer_parts))
    else:
        print("please add options from the list below:")
        for number, part in enumerate(availble_parts):
            print("{0}:\t{1}".format(number + 1, part))
        print("0:\tExit")
    current_choice = input()
print(computer_parts)
# Attempt 1
# choice = '-'
# computer_parts = []
# while choice != "0":
#     if choice in "12345":
#         print("Adding {} to computer parts".format(choice))
#         if choice == "1":
#             computer_parts.append("Computer")
#         elif choice == "2":
#             computer_parts.append("Monitor")
#         elif choice == "3":
#             computer_parts.append("Keyboard")
#         elif choice == "4":
#             computer_parts.append("Mouse")
#         elif choice == "5":
#             computer_parts.append("Floppy")
#         elif choice == "6":
#             computer_parts.append("HDMI Cable")
#     else:
#         print("Enter the value from below list: ")
#         print("1. Computer")
#         print("2. Monitor")
#         print("3. Keyboard")
#         print("4. Mouse")
#         print("5. Floppy")
#         print("6. HDMI Cable")
#         print("0. Exit")
#     choice = input()
# print("Computer parts: {}".format(computer_parts))

choice = '-'
computer_parts = []
available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Floppy",
                   "HDMI Cable"
                   ]

# valid_choice = ""
# for c in range(1, len(available_parts)+1):
#     valid_choice += str(c)
valid_choice = []
for c in range(1, len(available_parts)+1):
    valid_choice.append(str(c))

while choice != "0":
    if choice in valid_choice:
        if available_parts[int(choice)-1] in computer_parts:
            print("Removing {} from computer parts".format(choice))
            computer_parts.remove(available_parts[int(choice)-1])
            print("Requested parts {}".format(computer_parts))
        else:
            print("Adding {} from computer parts".format(choice))
            computer_parts.append(available_parts[int(choice)-1])
            print("Requested parts {}".format(computer_parts))

        # if choice == "1":
        #     computer_parts.append("Computer")
        # elif choice == "2":
        #     computer_parts.append("Monitor")
        # elif choice == "3":
        #     computer_parts.append("Keyboard")
        # elif choice == "4":
        #     computer_parts.append("Mouse")
        # elif choice == "5":
        #     computer_parts.append("Floppy")
        # elif choice == "6":
        #     computer_parts.append("HDMI Cable")
    else:
        print("Enter the value from below list: ")
        # The below code is not efficient, index function will search the full list and get the index
        # for part in available_parts:
        #     print("{}. {}".format(available_parts.index(part)+1, part))

        # Enumerate function returns the index and member at the same time
        for idx, part in enumerate(available_parts):
            print("{}. {}".format(idx +1, part))
        print("0. Exit")
    choice = input()
print("Computer parts ordered: {}".format(computer_parts))

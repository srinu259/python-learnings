computer_parts = [
    "monitor",
    "keyboard",
    "cpu",
    "mouse",
    "cable"
]

# this will replace the 3rd element and NOT append the list
computer_parts[3] = "usb"
print(computer_parts)

computer_parts[3:] = "usb"
print(computer_parts) # ['monitor', 'keyboard', 'cpu', 'u', 's', 'b']

computer_parts[3:] = ["speakers"]
print(computer_parts)

print(computer_parts[3:1:-1])
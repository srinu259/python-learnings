computer_parts = [
    "monitor",
    "keyboard",
    "cpu",
    "mouse",
    "cable"
]

computer_parts[3] = "usb"
print(computer_parts)

computer_parts[3:] = "usb"
print(computer_parts) # ['monitor', 'keyboard', 'cpu', 'u', 's', 'b']

computer_parts[3:] = ["speakers"]
print(computer_parts)
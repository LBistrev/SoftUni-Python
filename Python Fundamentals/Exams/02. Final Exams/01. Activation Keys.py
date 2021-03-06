activation_key = input()
new = ""
data = input()
while not data == "Generate":
    current_command = data.split(">>>")
    if current_command[0] == "Contains":
        substring = current_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command[0] == "Flip":
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if current_command[1] == "Upper":
            if start_index < len(activation_key) and end_index < len(activation_key):
                first_part = activation_key[:start_index]
                second = activation_key[start_index:end_index].upper()
                third = activation_key[end_index:]
                activation_key = first_part + second + third
                print(activation_key)
        elif current_command[1] == "Lower":
            if start_index < len(activation_key) and end_index < len(activation_key):
                first_part = activation_key[:start_index]
                second = activation_key[start_index:end_index].lower()
                third = activation_key[end_index:]
                activation_key = first_part + second + third
                print(activation_key)
    elif current_command[0] == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < len(activation_key) and end_index < len(activation_key):
            first = activation_key[:start_index]
            to_remove = activation_key[start_index:end_index]
            third = activation_key[end_index:]
            activation_key = first + third
            print(activation_key)
    data = input()

print(f"Your activation key is: {activation_key}")

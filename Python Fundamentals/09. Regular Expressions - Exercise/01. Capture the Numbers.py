import re

text = input()
pattern = r"\d+"
valid_nums = []
# for num in re.findall(pattern, text):
#    valid_nums.append(num)
while not text == "":
    valid_numbers = [number for number in re.findall(pattern, text)]
    valid_nums.extend(valid_numbers)
    text = input()
print(*valid_nums)

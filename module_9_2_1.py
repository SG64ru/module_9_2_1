first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# first_strings = [len(f_string) for f_string in first_strings if len(f_string) >= 5]
# print(first_strings)

second_strings = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
print(second_strings)

trird_result = {string:len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

print (trird_result)

first_strings = [len(f_string) for f_string in first_strings if len(f_string) >= 5]
print(first_strings)



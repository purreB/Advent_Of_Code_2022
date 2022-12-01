file = open('input.in', 'r')
lines = file.readlines()

most_calories = 0
elf_counter = 0
formatted_lines = []
current_sum_calories = 0

list_of_sums = []

for line in lines:
    ab = line.split()
    if len(ab) != 0:
        for i in range(len(ab)):
            ab[i] = int(ab[i])
    else:
        ab = 0
    formatted_lines.append(ab)

for item in formatted_lines:
    if item != 0:
        for i in range(len(item)):
            item[i] = int(item[i])
            current_calories = item[i]
            current_sum_calories = current_sum_calories + current_calories
    else:
        list_of_sums.append(current_sum_calories)
        current_sum_calories = 0


list_of_sums.sort()
top_3_elves = list_of_sums[248] + list_of_sums[249] + list_of_sums[250]

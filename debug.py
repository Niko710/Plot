list_instance = list(range(10))
new_list = []
tot_sum = 0

for index, value in enumerate(list_instance):
    new_list.append((index, value))
    tot_sum += value

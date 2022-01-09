import input as ipt

counter = 0
input_data = ipt.input
length = len(input_data)
int_list = []

for i, item in enumerate(input_data):
    if i+2 < length:
        temp_sum = input_data[i] + input_data[i+1] + input_data[i+2]
        int_list.append(temp_sum)

temp_len = len(int_list)

for i, item in enumerate(int_list):
    if i+1 < temp_len:
        if int_list[i+1] > int_list[i]:
            counter += 1


print(counter)
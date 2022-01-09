import input as ipt

counter = 0
input_data = ipt.input
length = len(input_data)

for i, item in enumerate(input_data):
    if i+1 < length:
        if input_data[i+1] > input_data[i]:
            counter += 1

print(counter)
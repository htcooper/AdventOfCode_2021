import input2 as ipt

up_counter = 0
down_counter = 0
forward_counter = 0

for item in ipt.input:
    for key in item:
        if key == 'up':
            up_counter += item[key]
        elif key == 'down':
            down_counter += item[key]
        elif key == 'forward':
            forward_counter += item[key]

final_depth = down_counter - up_counter
print(f"final depth is: {final_depth}")
print(f"final horizontal is: {forward_counter}")

mult = final_depth * forward_counter
print(f"result is {mult}")
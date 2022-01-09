import input2 as ipt

up_counter = 0
down_counter = 0
forward_counter = 0
aim = 0
depth = 0

for item in ipt.input:
    for key in item:
        if key == 'up':
            #up_counter += item[key]
            aim -= item[key]
        elif key == 'down':
            #down_counter += item[key]
            aim += item[key]
        elif key == 'forward':
            forward_counter += item[key]
            depth_incr = aim * item[key]
            depth += depth_incr

print(f"final horizontal is: {forward_counter}")

mult = depth * forward_counter
print(f"result is {mult}")
def readFile():
    master_list = []
    with open('input9.txt') as file:
        for line in file:
            numbers = [int(s) for s in line.strip()]
            master_list.append(numbers)
    return master_list

def isLow(value, coords, map):
    for c in coords:
        if map[c[0]][c[1]] <= value:
            return False

    return True

low_points = []
master_list = readFile()
width = len(master_list[0])
height = len(master_list)

for i,row in enumerate(master_list):
    for j,value in enumerate(row):

        coords = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
        if i == 0:
            coords.remove((i-1, j))
        elif i == height-1:
            coords.remove((i+1, j))
        if j == 0:
            coords.remove((i, j-1))
        elif j == width-1:
            coords.remove((i, j+1))

        if isLow(value, coords, master_list):
            low_points.append(value)
        
sum_list = sum(low_points)
risk = len(low_points)
total_risk = sum_list + risk

print(total_risk)
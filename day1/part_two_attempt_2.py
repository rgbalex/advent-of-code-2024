import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            if row:
                data.append(row)
    return data

if __name__ == "__main__":
    file_path = './day1/input_full.txt'
    data = read_csv(file_path)

print("Sanitizing input data...")

left = [int(data[i][0]) for i in range(len(data))]
right = [int(data[i][3]) for i in range(len(data))]

print("len(left):", len(left))
print("len(right):", len(right))
print("len(data):", len(data))

print("Ready to start.")

left.sort()
right.sort()

for i in range(10):
    pass
    print(left[i], right[i])

similarity = 0


left_occurrences = {}
right_occurrences = {}

for i in left:
    if i in left_occurrences:
        left_occurrences[i] += 1
    else:
        left_occurrences[i] = 1

for i in right: 
    if i in right_occurrences:
        right_occurrences[i] += 1
    else:
        right_occurrences[i] = 1

print("left_occurrences:", left_occurrences)

print("right_occurrences:", right_occurrences)

# print the max value in right dictionary
max_right = max(right_occurrences, key=right_occurrences.get)
print("max_right:", max_right)
print("right_occurrences[max_right]:", right_occurrences[max_right])
# and print its corresponding value

# the input data's left list contains only unique values, so we can cheat calculating 
# the similarity score. 

for i in left_occurrences.keys():
    if i in right_occurrences:
        similarity += i * right_occurrences[i]

print("similarity:", similarity)
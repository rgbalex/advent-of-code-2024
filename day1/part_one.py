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
    file_path = './day1/input.txt'
    data = read_csv(file_path)

print("Sanitizing input data...")

left = [data[i][0] for i in range(len(data))]
right = [data[i][3] for i in range(len(data))]

print("len(left):", len(left))
print("len(right):", len(right))
print("len(data):", len(data))

print("Ready to start.")

left.sort()
right.sort()

for i in range(10):
    pass
    # print(left[i], right[i])

difference = 0
for i in range(len(left)):
    difference += abs(int(right[i]) - int(left[i]))

print("Difference:", difference)


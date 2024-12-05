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

similarity = 0
i = 0
j = 0

is_same = False

try:
    while True:
        if is_same:
            last_seen = int(left[i])
            occurrence = 0
            while left[i] == right[j]:
                occurrence += 1
                j += 1
                
            similarity_increase = int(left[i]) * occurrence
            print("i:", i, "j:", j, "last_seen:", last_seen, "occurrence:", occurrence, "similarity_increase:", similarity_increase)
            
            left_occurrences = 0
            while int(left[i]) == last_seen:
                left_occurrences += 1
                i += 1
            
            print("left_occurrences:", left_occurrences)
            similarity += similarity_increase * left_occurrences

            is_same = False
        else:    
            if int(left[i]) == int(right[j]):
                is_same = True
            elif int(left[i]) < int(right[j]):
                i += 1
            else:
                j += 1
except IndexError as e:
    if i > len(left) - 1:
        print("Finished. Reached end of left list.")
    elif j > len(right) - 1:
        print("Finished. Reached end of right list.")
    else:
        print("Error:", e)
finally:
    print("i:", i, "j:", j, "last_seen", last_seen, "occurrence:", occurrence, "similarity_increase:", similarity_increase)
    print("left_occurrences:", left_occurrences)
    similarity += similarity_increase * left_occurrences
    print("i:", i, "j:", j)
    # print the last 10 elements of the lists
    print("left:", left[-20:])
    print("right:", right[-20:])
    
print("Similarity:", similarity)
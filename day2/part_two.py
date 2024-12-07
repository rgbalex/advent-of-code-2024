import csv

data = []
file_path = './day2/input.txt'

with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        if row:
            row = [int(i) for i in row]
            data.append(row)

print("Data loaded.")

valid_counter = 0
row_counter = 1
# for entry in data[978::979]:
for entry in data:
    print(f"Row: {row_counter} Entry: {entry}")
    row_counter += 1
    i = iter(entry)
    one = next(i)
    two = next(i)
    
    # print("One: ", one)
    # print("Two: ", two)
    
    run = True
    removed_one = False

    if one < two:
        if 0 < two - one <= 3:
            # print("Valid")
            pass
        else:
            if removed_one == False:
                removed_one = True
                continue
            print("Invalid")
            run = False

        while run == True:
            try: 
                one = two
                two = next(i)
                if 0 < two - one <= 3:
                    # print("Valid")
                    pass
                else:
                    if removed_one == False:
                        removed_one = True
                        continue
                    print("Invalid")
                    run = False
            except StopIteration:
                valid_counter += 1
                run = False
    elif two < one:
        if 0 < one - two <= 3:
            # print("Valid")
            pass
        else:
            if removed_one == False:
                removed_one = True
                continue
            print("Invalid")
            run = False

        while run == True:
            try: 
                one = two
                two = next(i)
                if 0 < one - two <= 3:
                    # print("Valid")
                    pass
                else:
                    if removed_one == False:
                        removed_one = True
                        continue
                    print("Invalid")
                    run = False
            except StopIteration:
                valid_counter += 1
                run = False
    elif one == two:
        # if removed_one == False:
            # removed_one = True
            # continue
        print("Equal, and invalid")
        break
    else:
        print("Error")
        raise NotImplementedError("This should not happen.")
print("Valid counter: ", valid_counter)
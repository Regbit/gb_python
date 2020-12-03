num_str = input("Enter your number: ")
largest = 0
while int(num_str) != 0:
    if int(num_str) % 10 > largest:
        largest = int(num_str) % 10
        if largest == 9:
            break
    num_str = "{}".format(int(num_str) // 10)

print("Largest:", largest)
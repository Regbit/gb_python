total_sec = int(input("Enter your time in seconds:"))

display_sec = total_sec % 60
display_min = total_sec // 60 % 60
display_hours = total_sec // 60 // 60

print("{:02d}:{:02d}:{:02d}".format(display_hours, display_min, display_sec))
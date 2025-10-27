

time_input = int(input("Input time in seconds (0 - 8640000): "))

days = time_input // 86400
rem = time_input % 86400

hours = rem // 3600
rem = rem % 3600

minutes = rem // 60
seconds = rem % 60

if time_input < 0 or time_input > 8640000:
    print("Invalid number")
else:
    print(f"Days:{days}, hours {hours}, minutes {minutes}, seconds {seconds}")

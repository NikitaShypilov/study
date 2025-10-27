

time_input = int(input("Input time in seconds (0 - 8640000): "))

days = time_input // 86400
rem = time_input % 86400

hours = rem // 3600
rem = rem % 3600

minutes = rem // 60
seconds = rem % 60

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"


if time_input < 0 or time_input > 8640000:
    print("Invalid number")
else:
    print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")


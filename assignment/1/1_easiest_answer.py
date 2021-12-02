from datetime import datetime

answer = 0
target_month = 1


def generate_day(y, d):
    try:
        return datetime(y, target_month, d).weekday()
    except ValueError:
        return None


for y in range(1900, 2001):
    for d in range(1, 32):
        day = generate_day(y, d)
        if day and day == 6:
            answer += 1

print(answer)



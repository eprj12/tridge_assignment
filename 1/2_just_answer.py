def get_day_of_the_week(cnt):
    day_of_the_week = {
        0: 'MONDAY',
        1: 'TUESDAY',
        2: 'WENDESDAY',
        3: 'THURSDAY',
        4: 'FRIDAY',
        5: 'SATURDAY',
        6: 'SUNDAY'
    }

    return day_of_the_week[cnt % 7]


def get_day_of_month(year, month):
    day_of_month = {
        1: 31,
        2: 28 if not (year // 4) and (year // 400) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return day_of_month[month]


class DayInfo:
    def __init__(self, year, month, day, day_of_week=None):
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week


plain_list = []

day_of_the_week_count = 0
answer = 0
for y in range(1900, 2001):
    for m in range(1, 13):
        end_of_month = get_day_of_month(y, m)
        for d in range(1, end_of_month + 1):
            d_info = DayInfo(
                year=y,
                month=m,
                day=d,
                day_of_week=get_day_of_the_week(day_of_the_week_count)
            )

            plain_list.append(d_info)

            if m == 1 and d_info.day_of_week == 'SUNDAY':
                answer += 1

            day_of_the_week_count += 1

print(answer)
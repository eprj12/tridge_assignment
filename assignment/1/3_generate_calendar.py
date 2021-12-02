from collections import OrderedDict

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


class Year:
    def __init__(self, year):
        self.year = year
        self.month = OrderedDict()


class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.day = OrderedDict()


class Day:
    def __init__(self, year, month, day, day_of_week):
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week


class Calendar:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
        self.year_info = OrderedDict()
        self.generate_calendar(self)

    @staticmethod
    def generate_calendar(self):
        day_of_week_count = 0
        for y in range(self.start_year, self.end_year + 1):
            current_year = Year(year=y)
            for m in range(1, 13):
                current_month = Month(year=y, month=m)
                end_of_month = get_day_of_month(y, m)
                for d in range(1, end_of_month + 1):
                    current_day = Day(y, m, d, get_day_of_the_week(day_of_week_count))
                    day_of_week_count += 1
                    current_month.day[d] = current_day
                current_year.month[m] = current_month
            self.year_info[y] = current_year


answer = 0
calendar = Calendar(1900, 2000)

for year, y_info in calendar.year_info.items():
    january = y_info.month[1]
    days = january.day
    sunday_count = len([d for d, d_info in days.items() if d_info.day_of_week == 'SUNDAY'])
    answer += sunday_count

print(answer)

"""
https://leetcode.com/problems/reformat-date/
1507. Reformat Date
"""


class Solution:
    def reformatDate(self, s: str) -> str:
        months = {
            "Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
            "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'
        }

        def get_date(my_day):
            day = my_day[2]
            removed_last_two_char = day[0:len(day) - 2]
            if int(removed_last_two_char) < 10:
                return "0" + str(removed_last_two_char)
            return str(removed_last_two_char)

        def get_month(my_day):
            return months[my_day[1]]

        def get_year(my_day):
            return my_day[0]

        date = s.split(" ")[::-1]
        year = get_year(date)
        month = get_month(date)
        day = get_date(date)

        return f'{year}-{month}-{day}'

    def reformatDate2(self, s: str) -> str:
        month = {
            "Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
            "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'
        }

        date = s.split(" ")[::-1]
        result = []
        for each in date:
            if each in month:
                result.append(month[each])
            else:
                temp = []
                for char in each:
                    if char.isnumeric():
                        temp.append(char)
                if len(temp) == 1:
                    temp.insert(0, "0")
                result.append("".join(temp))
        return "-".join(result)

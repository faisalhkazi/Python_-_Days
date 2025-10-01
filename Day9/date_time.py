# import datetime
#
# my_time = datetime.time(15, 33, 54)
#
# print(my_time)
#
# my_day = datetime.date(2025, 10, 6)
#
# print(my_day.today())
import time
from datetime import *

# my_date = datetime(2025, 10, 6, 5, 15, 55, 1400)
#
# my_date = my_date.replace(month=11)
#
# print(my_date)
#
# birth = datetime(1991, 4, 27, 15, 33, 45)
#
# death = datetime(2055, 4, 27, 15, 33, 45)
#
# total_life = death - birth
#
# years = total_life.days / 365

#
# print(int(years))

current_miniutes = datetime.now().minute

print(current_miniutes)
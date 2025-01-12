import time
from calendar import isleap


def set_leapyear(year):
    if isleap(year):
        return True
    else:
        return False


def day_mounth(mounth, yearleap):
    if mounth in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mounth in [4, 6, 9, 11]:
        return 30
    elif mounth == 2 and yearleap:
        return 29
    elif mounth == 2 and (not yearleap):
        return 28


name = input("Type your name: ")
age = input("Type your age: ")
localtime = time.localtime(time.time())
year = int(age)
mounth = year * 12 + localtime.tm_mon
day = 0
start_year = int(localtime.tm_year) - year
end_year = start_year + year

for y in range(start_year, end_year):
    if set_leapyear(y):
        day = day + 366
    else:
        day = day + 365

yearleap = set_leapyear(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + day_mounth(m, yearleap)

    day = day + localtime.tm_mday
print("Age of %s is years or " % (name, year), end="")
print("%d mounths or %d days" % (mounth, day))

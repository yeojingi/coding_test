import datetime


# Month DD, YYYY HH:MM
i = 1
MONTHS = {}
for month in list("January, February, March, April, May, June, July, August, September, October, November, December".split(", ")):
  MONTHS[month] = i
  i += 1
s = list(input().split(' '))
month = MONTHS[s[0]]
dd = int(s[1][:-1])
yyyy = int(s[2])
hh, mm = map(int, s[3].split(':'))

theDate = datetime.datetime(yyyy, month, dd, hh, mm)
lastDate = datetime.datetime(yyyy+1, 1, 1, 0, 0)
firstDate = datetime.datetime(yyyy, 1, 1, 0, 0)

result = theDate-firstDate
gross = lastDate-firstDate
print((result.total_seconds())/gross.total_seconds()*100)
import time
from datetime import datetime

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
# dt3 = datetime.strptime("2018/01/01", "&Y/%m/%d")
dt4 = datetime.fromtimestamp(time.time())
print(dt1)
print(dt2)
print(dt4)
print(f"{dt1.year}/{dt1.month}/{dt1.day}")
print(dt1.strftime("%Y/%m"))

print(dt2 > dt1)
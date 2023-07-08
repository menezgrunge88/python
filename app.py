from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

#now = now + relativedelta(month=10, day=12, hour=7)
print(now)



print(relativedelta(datetime(2023, 7, 8, 2, 0, 0), now))
print(relativedelta(now, datetime(2023, 7, 8, 2, 0, 0)))
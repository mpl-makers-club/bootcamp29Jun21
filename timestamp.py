# timestamp.py
import datetime

now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")

print(date_stamp)

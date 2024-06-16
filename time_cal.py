#s24018
#現在の時刻と2024年6月のカレンダーを表示する

import calendar as cal
import datetime
now = datetime.datetime.now()
print(cal.month(2024,6))
print(now.strftime("%Y年%m月%d日　%H:%M:%S"))

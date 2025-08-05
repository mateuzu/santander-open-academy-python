import pytz
from datetime import datetime, timezone, timedelta

# Com PITZ
date_time = datetime.now()
print(date_time)
date_sao_paulo = date_time(pytz.timezone("America/Sao_Paulo"))
print(date_sao_paulo)
date_time_oslo = date_time(pytz.timezone("Europe/Oslo"))
print(date_time_oslo)

# Com datetime
data_time_2 = datetime.now()
date_sao_paulo_2 = data_time_2(timezone(timedelta(hours=-3)))
print(date_sao_paulo_2)
date_time_oslo_2 = data_time_2(timezone(timedelta(hours=2)))
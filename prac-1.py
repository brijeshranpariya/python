from datetime import datetime
import pytz

start_date = "2025-12-10"
end_date = "2025-12-15"

est_tz = pytz.timezone("US/Eastern")

today_date_utc = datetime.now(pytz.utc)
today_date = datetime.now(pytz.utc).astimezone(est_tz)

start_dt = est_tz.localize(datetime.strptime(start_date, "%Y-%m-%d"))
end_dt = est_tz.localize(datetime.strptime(end_date, "%Y-%m-%d")).replace(
    hour=23, minute=59, second=59
)


is_within_range = start_dt <= today_date <= end_dt
print(f"today_date (EST) : {today_date}")
print("Within range:", is_within_range)
if is_within_range:
    weekday = today_date.weekday()
    print(weekday)
    if weekday < 5:
        print("Within range and it's a weekday (Mon–Fri)")
        is_weekday = True
        is_weekend = False
    else:
        print("Within range and it's a weekend (Sat–Sun)")
        is_weekday = False
        is_weekend = True
else:
    print("Not within date range")
    is_weekday = False
    is_weekend = False

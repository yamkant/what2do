from datetime import datetime
import pytz

korea_tz = pytz.timezone("Asia/Seoul")

def now():
    return datetime.now(korea_tz)

def get_current_time():
    current_time = now()
    return datetime(
        year=current_time.year,
        month=current_time.month,
        day=current_time.day,
        hour=current_time.hour,
        minute=current_time.minute,
        second=current_time.second
    )

def combine_datetime_to_now(value):
    return datetime.combine(now(), value)
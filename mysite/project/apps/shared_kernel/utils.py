from datetime import datetime

def get_current_time():
    current_time = datetime.now()
    return datetime(
        year=current_time.year,
        month=current_time.month,
        day=current_time.day,
        hour=current_time.hour,
        minute=current_time.minute,
        second=current_time.second
    )

def combine_datetime_to_now(value):
    # ret = datetime.combine(now(), value)
    print(datetime.now())
    ret = datetime.now().replace(hour=value.hour, minute=value.minute, second=value.second)
    return ret
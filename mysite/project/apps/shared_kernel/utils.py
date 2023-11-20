import datetime
import pytz

korea_tz = pytz.timezone("Asia/Seoul")

def now():
    return datetime.datetime.now(korea_tz)
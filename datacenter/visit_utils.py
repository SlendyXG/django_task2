from django.utils.timezone import localtime

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = localtime() - visit.entered_at
    return int(duration.total_seconds())


def format_duration(duration):
    hours = duration // SECONDS_IN_HOUR
    minutes = (duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = duration % SECONDS_IN_MINUTE
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > minutes * SECONDS_IN_MINUTE
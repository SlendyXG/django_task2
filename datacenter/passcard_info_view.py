from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
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


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    this_passcard_visits = []
    for visit in visits:
        duration_seconds = get_duration(visit)

        visit_data = {
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration_seconds),
            'is_strange': is_visit_long(visit, minutes=60),
        }
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }

    return render(request, 'passcard_info.html', context)
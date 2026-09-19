from django.shortcuts import render, get_object_or_404

from datacenter.models import Passcard, Visit
from datacenter.visit_utils import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }

    return render(request, 'passcard_info.html', context)
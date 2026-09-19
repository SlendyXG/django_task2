from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from datacenter.visit_utils import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        }
        for visit in active_visits
    ]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
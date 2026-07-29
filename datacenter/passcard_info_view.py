from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = localtime() - visit.entered_at
    return int(duration.total_seconds())


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    if hours > 0:
        return f"{hours}ч {minutes}м"
    return f"{minutes}м"


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > minutes * 60


def passcard_info_view(request, passcode):
    # 1. Получаем пропуск по passcode из URL
    passcard = get_object_or_404(Passcard, passcode=passcode)

    # 2. Получаем все визиты этого пропуска
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    # 3. Формируем список визитов для шаблона
    this_passcard_visits = []
    for visit in visits:
        duration_seconds = get_duration(visit)

        visit_data = {
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration_seconds),
            'is_strange': is_visit_long(visit, minutes=60),
        }
        this_passcard_visits.append(visit_data)

    # 4. Формируем контекст (словарь с данными для шаблона)
    context = {
        'passcard': passcard,  # <-- передаем пропуск
        'this_passcard_visits': this_passcard_visits  # <-- передаем список визитов
    }

    # 5. Рендерим шаблон с контекстом
    return render(request, 'passcard_info.html', context)
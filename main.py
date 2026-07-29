import os

from django.core.management import execute_from_command_line
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from datacenter.models import Visit, Passcard


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = localtime() - visit.entered_at
    return int(duration.total_seconds())


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    return f"{hours}ч {minutes}м"


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > minutes * 60


if __name__ == "__main__":
    all_visits = Visit.objects.all()

    # Только для 10 и 1000 минут
    test_values = [1001]

    for minutes in test_values:
        long_visits = [visit for visit in all_visits if is_visit_long(visit, minutes)]
        # Формируем список визитов с информацией о времени выхода
        visit_strings = []
        for visit in long_visits:
            if visit.leaved_at:
                exit_time = visit.leaved_at.strftime("%H:%M")
                visit_strings.append(
                    f"{visit.passcard.owner_name} вошел в {visit.entered_at.strftime('%H:%M')}, вышел в {exit_time}")
            else:
                visit_strings.append(
                    f"{visit.passcard.owner_name} вошел в {visit.entered_at.strftime('%H:%M')}, еще внутри")

        print(f"Визиты дольше {minutes} мин [{', '.join(visit_strings)}]")


    #passcard = Passcard.objects.all()[1]
    #print(passcard.owner_name)
    #visits = Visit.objects.filter(passcard=passcard)
    #print(visits)

    execute_from_command_line(['manage.py', 'runserver'])
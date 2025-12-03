from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Task

@shared_task
def check_deadlines():
    now = timezone.now()
    one_hour_later = now + timezone.timedelta(hours=1)

    # Get tasks with deadline within the next hour that haven't been reminded
    tasks = Task.objects.filter(
        deadline__gte=now,
        deadline__lte=one_hour_later,
        is_completed=False,
        reminder_sent=False
    )

    # If no tasks in the next hour, try any incomplete tasks with deadlines (for testing)
    if not tasks.exists():
        tasks = Task.objects.filter(
            deadline__isnull=False,
            is_completed=False,
            reminder_sent=False
        )[:5]  # Limit to 5 for testing

    for t in tasks:
        # Calculate remaining time
        if t.deadline:
            remaining = t.deadline - now
            hours = remaining.total_seconds() // 3600
            minutes = (remaining.total_seconds() % 3600) // 60
            time_left = f"{int(hours)} часов {int(minutes)} минут"
        else:
            time_left = "Нет информации"
        
        message = f"""
Привет {t.user.first_name or t.user.username}!

Напоминание о задаче: {t.title}

Осталось времени: {time_left}

Описание: {t.description or 'Нет описания'}

Пожалуйста, выполните задачу вовремя!

С уважением,
Todo App
        """
        
        try:
            send_mail(
                subject=f"⏰ Напоминание о дедлайне: {t.title}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[t.user.email],
                fail_silently=False
            )
            t.reminder_sent = True
            t.save()
            print(f"✓ Email sent for task: {t.title} to {t.user.email}")
        except Exception as e:
            print(f"✗ Error sending email for task {t.id}: {str(e)}")

    return f"Sent notifications: {tasks.count()}"

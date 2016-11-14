from django.core.management.base import BaseCommand, CommandError
from gst.models import Category, Task, SubTask
from django.contrib.auth.models import User
from django.utils import timezone
import smtplib


def is_deadline_near(date):
    if date > timezone.now():
        delta = date - timezone.now()
        return delta.days == 0

class Command(BaseCommand):
    help = 'Checks for tasks/subtasks near deadlines and notify users.'

    def handle(self, *args, **options):
        for user in User.objects.all():
            deadlines = []
            for category in user.category_set.all():
                for task in category.task_set.all():
                    if (task.notify_user and not task.complete and
                        is_deadline_near(task.deadline)):
                        deadlines.append(task)
                    for subtask in task.subtask_set.all():
                        if (subtask.notify_user and not subtask.complete and
                            is_deadline_near(subtask.deadline)):
                            deadlines.append(subtask)

                if len(deadlines) > 0:
                    deadline_names = ''
                    for deadline in deadlines:
                        deadline_names = deadline_names + '\n' + str(deadline.name)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('slemankassis@gmail.com', '')
                    message = 'For user {0} found {1} tasks and subtasks near deadlines: \n {2}'.format(user.username, len(deadlines), deadline_names)
                    server.sendmail('slemankassis@gmail.com', 'slemankassis@gmail.com', message)
                    server.quit()
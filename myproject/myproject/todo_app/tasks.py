from celery import shared_task


@shared_task
def execute_reminder(todo_id):
    pass

# core/tasks.py
from celery import shared_task
from .models import Admission

@shared_task
def update_admission_status(admission_id, status):
    try:
        admission = Admission.objects.get(id=admission_id)
        admission.status = status
        admission.save()
    except Admission.DoesNotExist:
        pass

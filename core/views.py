# core/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee, Patient, Admission, Allocation
from .serializers import PatientSerializer, AdmissionSerializer, AllocationSerializer
from datetime import timedelta

@api_view(['GET'])
def patients_by_staff(request, id):
    allocations = Allocation.objects.filter(employee_id=id)
    admission_ids = allocations.values_list('admission_id', flat=True)
    admissions = Admission.objects.filter(id__in=admission_ids)
    patient_ids = admissions.values_list('patient_id', flat=True)
    patients = Patient.objects.filter(id__in=patient_ids)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def discharged_patients(request):
    admissions = Admission.objects.all()
    discharged_patients = [
        admission for admission in admissions if (admission.discharge_date - admission.admission_date) <= timedelta(days=3)
    ]
    patient_ids = [admission.patient_id.id for admission in discharged_patients]
    patients = Patient.objects.filter(id__in=patient_ids)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def day_with_most_admissions(request):
    admissions = Admission.objects.all()
    days = [admission.admission_date.weekday() for admission in admissions]
    most_common_day = max(set(days), key=days.count)
    return Response({'week': most_common_day})

@api_view(['GET'])
def avg_duration_by_staff(request, id):
    allocations = Allocation.objects.filter(employee_id=id)
    admissions = [Allocation.objects.get(id=allocation.admission_id.id) for allocation in allocations]
    durations = [(admission.discharge_date - admission.admission_date).days for admission in admissions if admission.discharge_date]
    average_duration = sum(durations) / len(durations) if durations else 0
    return Response({'duration': average_duration})

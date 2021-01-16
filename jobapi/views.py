from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer

from .models import Job
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Get Job List':'/job-list/',
        'Get a Job By Company Name':'/job-detail/<str:pk>/',
        'Create a Job':'/job-create/',
        'Update a Job By Id':'/job-update/<str:pk>/',
        'Delete a Job By Id':'/job-delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def jobList(request):
    filters = {}
    companyName = request.GET.get('companyName', "")
    size = int(request.GET.get("size", 10))
    page = int(request.GET.get("page", 0))

    if page > 0:
        size = size * (page + 1)

    if len(companyName.strip()) > 0:
        filters['company_name'] = companyName

    jobs = Job.objects.filter(**filters).order_by('-job_id')[page * int(request.GET.get("size", 10)):size]
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def jobCreate(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def jobUpdate(request, pk):
    job = Job.objects.get(job_id=pk)
    serializer = JobSerializer(instance=job, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def jobDelete(request, pk):
    job = Job.objects.get(job_id=pk)
    job.delete()

    return Response('Item succsesfully delete!')




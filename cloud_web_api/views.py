from django.http import JsonResponse
from .models import Kisi
from .serializers import KisiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def Kisi_list(request):
    if request.method == 'GET':
        #eleman_ekle()
        kisiler = Kisi.objects.all()
        serializer = KisiSerializer(kisiler, many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer = KisiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
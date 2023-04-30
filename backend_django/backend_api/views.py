from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InfoBlog
from .serializer import InfoBlogSerializer

class InfoBlogView(APIView):
    def get(self,request):
        output = [
            {
                "title" : output.title,
                "info" : output.info
            } for output in InfoBlog.objects.all()
        ]
        return Response(output)
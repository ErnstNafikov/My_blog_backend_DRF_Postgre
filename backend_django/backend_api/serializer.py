from rest_framework import serializers
from .models import InfoBlog

class InfoBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBlog
        fields = ['title', 'info']
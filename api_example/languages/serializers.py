# 직렬 변환기 파일
from rest_framework import serializers
from .models import Language

# rest_framwork에서 가장 일반적인 모델 직렬 변환기
# HyperlinkedModelSerializer라고 해도 되긴 하다
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')
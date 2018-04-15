from rest_framework import serializers
from testing.models import Test, Result
from django.contrib.auth.models import User


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'question', 'answers', 'correct_answer')


class ResultSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Result
        fields = ('id', 'question_count', 'correct_answer_count', 'owner')


class UserSerializer(serializers.ModelSerializer):
    results = serializers.PrimaryKeyRelatedField(many=True, queryset=Result.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'results')

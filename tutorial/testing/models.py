from django.db import models


class Test(models.Model):
    question = models.CharField(max_length=200)
    answers = models.CharField(max_length=800)
    correct_answer = models.CharField(max_length=200)


class Result(models.Model):
    question_count = models.IntegerField()
    correct_answer_count = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='results', on_delete=models.CASCADE)

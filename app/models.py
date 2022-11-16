from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    value = models.CharField(max_length=25)


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField
    upvote_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
  
class Answer(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField
    isCorrect = models.BooleanField(default=False)
    upvote_count = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)

class Profile(models.Model):
    avatar = models.ImageField
    nickname = models.CharField(max_length=15)
    owner = models.OneToOneField(User, on_delete=models.RESTRICT)
    
    
QUESTIONS = [
    {
        'id':   question_id,
        'title': f'Question#{question_id}',
        'text': f'Text of question#{question_id}',
        'answers_number': question_id * question_id,
        'tags': ['tag' for i in range(question_id)],
        'answers': 5,
    }    for question_id in range(100)
]


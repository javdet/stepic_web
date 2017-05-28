from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT title, text, added_at, rating, author, likes 
            FROM qa_question ORDER BY added_at DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(title=row[0], 
                          text=row[1], 
                          added_at=row[2], 
                          rating=row[3],
                          author=row[4],
                          likes=row[5]
            )
            result_list.append(p)
        return result_list

    def popular(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT title, text, added_at, rating, author, likes 
            FROM qa_question ORDER BY rating DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(title=row[0], 
                          text=row[1],  
                          added_at=row[2],  
                          rating=row[3],
                          author=row[4],
                          likes=row[5]
            )
            result_list.append(p)
        return result_list


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Answer)
    QuestionManager = models.Manager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

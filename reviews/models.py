from django.db import models


class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    title = models.TextField('글제목', max_length=1000)
    contents = models.TextField('글내용', max_length=1000)
    created_date = models.DateField('작성시간')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    created_date = models.DateField('작성시간')

    def __str__(self):
        return self.text
from django import forms                  # 장고가 제공해주는 forms 와
from reviews.models import Post, Comment    # 만들어 놓은 모델을 이용해서 ModelForm class 를 만든다


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'contents']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

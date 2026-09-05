from django.db import models
from app.profile.model import Profile
from app.article.model import Article

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
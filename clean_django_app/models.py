from django.db import models

class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.name} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class Author(BaseTimestampModel):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Bio: {self.bio[:20]}...)" if self.bio else self.name

class Category(BaseTimestampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(BaseTimestampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




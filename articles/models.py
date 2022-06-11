from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="articles"
    )

    def __str__(self):
        return f"{self.title} by {self.author}"

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=100)
    body = models.TextField(blank=True, default="")
    slug = models.SlugField(max_length=200, unique_for_date='published')
    published = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return f"{self.title}"


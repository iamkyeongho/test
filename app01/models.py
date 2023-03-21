from django.db import models

# Create your models here.

class Blog(models.Model):
    subject = models.CharField(max_length=45, null=False)
    ctx_text = models.TextField(null=True, blank=True)
    ctx_image = models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "블로그"


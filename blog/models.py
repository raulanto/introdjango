from django.db import models
from datetime import datetime

class Post(models.Model):
    not_title = models.CharField(max_length=200)
    not_body=models.TextField()
    not_created_at=models.DateTimeField(default=datetime.now,blank=True)
    not_fk_user=models.IntegerField()

    def __str__(self):
        return self.not_title
    
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        verbose_name_plural = 'Post'
from django.db import models

class Note(models.Model):
    subject = models.CharField(max_length=100)
    semester = models.IntegerField()
    module = models.IntegerField()
    department = models.CharField(max_length=100)
    file = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.subject
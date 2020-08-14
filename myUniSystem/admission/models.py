from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
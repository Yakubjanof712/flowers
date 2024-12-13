from django.db import models

class Type(models.Model):  # Turlar
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flower(models.Model):  # Gullar
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='flowers')

    def __str__(self):
        return self.name

from django.db import models


class FrameworkModel(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FrameworkModel'
        verbose_name_plural = 'FrameworkModels'

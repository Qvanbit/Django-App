from django.db import models

class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
        )

    class Meta:
        abstract = True
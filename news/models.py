from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=250
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name="Фото",
    )
    created_at = models.DateField(
        verbose_name="Дата создание",
        auto_created=True,
    )
    author = models.CharField(
        verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return f"{self.title}"


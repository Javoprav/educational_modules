from django.db import models
NULLABLE = {'null': True, 'blank': True}


class Module(models.Model):
    """Модель описывающая Образовательные модули"""
    number = models.PositiveIntegerField(unique=True, verbose_name='порядковый номер')
    name = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='module/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=15000, verbose_name='описание', **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлен', **NULLABLE)

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'

    def __str__(self):
        return f'{self.name}'

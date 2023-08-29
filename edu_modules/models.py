from django.db import models
NULLABLE = {'null': True, 'blank': True}


class Module(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='порядковый номер')
    name = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлен', **NULLABLE)

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'

    def __str__(self):
        return f'{self.name}'

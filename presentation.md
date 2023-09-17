# Презентация
       
## Описание задачи:
#### Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:
    • порядковый номер 
    • название 
    • описание 

## Задача

### При создании проекта нужно:
####     1. реализовать для модели (моделей) все методы CRUD
####     2. Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

## Требуемый стэк
    • python 3.11 
    • Docker 
    • Django 

### Условия приемки
    • код размещен в открытом репозитории 
    • доступна документация 
    • код покрыт автоматизированными юнит-тестами 
    • код оформлен согласно pep8 
    • оформлен Readme файл 
    • в проекте использован Docker 

____________________________________________________________

## Выбраны версии продукта:
    • Python: 3.11  - Язык программирования.
    • Django: 4.2.4  - Основной фреймворк для веб-приложения.
    • Django Rest Framework: 3.14 - Расширение Django для создания RESTful API.
    • Docker: 6.1.3 Изоляция и управление контейнерами.
    • PostgreSQL: База данных.


### Создан проект Django и DRF. Создана модель "Образовательные модули" с полями для порядкового номера, названия и описания.

```python
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
```
### Реализованы все методы CRUD для модели "Образовательные модули", что позволяет создавать, читать, обновлять и удалять записи. Для этого использованы классы-виды (viewsets) DRF.

```python
class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    pagination_class = ModulesPagination
```
       
### Создан сериализатор для модели "Образовательные модули". Сериализатор позволят преобразовывать данные модели в JSON и обратно.

```python
class ModulesSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Module"""
    class Meta:
        model = Module
        fields = "__all__"
```

### Создана модель "Пользователь" с возможностью регистрации по почте.

```python
class User(AbstractUser):
    """Модель описывающая Пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль',
                            **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активность')
```

### Реализованы все методы CRUD, что позволяет создавать, читать, обновлять и удалять записи. Для этого использованы классы-виды (generics) DRF.


```python
class UsersListView(generics.ListAPIView):
    """Контроллер для списка пользователей"""
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
```

### Валидаторы

    • Создан валидатор на минимальное описание модуля в 100 символов

### Права доступа

    • Каждый пользователь имеет доступ ко всем модулям, может создавать новые модули. Редактирование и удаление доступно только модератору и суперюзеру.
    • Аналогичные доступы у модели пользователя, но с доступом на редактирование своих данных.


### Используется PostgreSQL для хранения данных моделей.

### Создан Docker Compose для запуска проекта в контейнерах Docker, который включает в себя контейнер с базой данных, контейнер с приложением Django и контейнер с сервером Nginx.

### Документация. Использован инструмент документирования Swagger. 

### http://158.160.105.158/swagger/

### Код соответствует стандартам оформления PEP 8. 

```bash
flake8 --exclude=venv,migrations --ignore=E501
```

### Создан файл README с описанием проекта, инструкциями по развертыванию и использованию.

### Добавлена пагинация для лучшего пользования проектом (выводит 2 объекта на страницу)

### Создано два репозитория GitHub и GitLab, с открытым доступом:

### https://github.com/Javoprav/educational_modules.git

### https://gitlab.com/javoprav/educational_modules

### Написаны юнит-тесты (unittest), которые полностью покрывают модель "Образовательные модули", сериализаторы и виды. Использована библиотека unittest. Все тесты были успешно пройдены, что гарантирует правильное функционирование приложения.

### Демонстрация на сервере:

```bash
ssh admin@158.160.105.158

cd opt/educational_modules/

sudo docker-compose -f docker-compose.prod.yml exec api python3 manage.py test --verbosity 2
```

## Postman (демонстрация):

http://158.160.105.158/api/token/

## Web (демонстрация):

http://158.160.105.158/api/token/

## Доп. задание

### Приложение "Образовательные модули" обеспечивает легкую интеграцию с другими системами и технологиями, что делает его универсальным инструментом для проектов образовательного характера. Это сокращает время внедрения приложения с 2 недель до 3 - 5 дней.

### Оно может быть легко настроено и адаптировано к специфическим требованиям и потребностям любого учебного заведения, обеспечивая гибкость и эффективность работы.


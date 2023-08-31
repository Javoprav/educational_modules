from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Команда для создания суперюзера"""
        user = User.objects.create(
            email='admin5@gmail.com',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('123')
        user.save()

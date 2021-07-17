from users.models import UserProfile
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')
        parser.add_argument('-p', '--prefix', type=str, help='Префикс для username')
        parser.add_argument('-a', '--admin', action='store_true', help='Создание учетной записи администратора')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                UserProfile.objects.create_superuser(username=username, email=get_random_string()+'@', password='123')
            else:
                UserProfile.objects.create_user(username=username, email=get_random_string()+'@', password='123')



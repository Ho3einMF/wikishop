import factory

from apps.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.sequence(lambda n: f'user-{n + 1}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.PostGenerationMethodCall('set_password', 'abcxyz123')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

import random

import factory

from apps.accounts.tests.factories import UserFactory
from apps.content.models import Post, Category


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'category-{n}')


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Faker('paragraph')
    caption = factory.Faker('text')
    price = random.randint(1000, 10000)

    # Foreign Key Fields
    # publisher = factory.SubFactory(UserFactory)
    # category = models.ForeignKey(to='content.Category', on_delete=models.PROTECT, related_name='posts')

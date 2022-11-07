import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from apps.accounts.tests.factories import UserFactory
from apps.content.models import Category, Post, Score


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'category-{n}')


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Faker('company')
    caption = factory.Faker('text')
    price = FuzzyInteger(1000, 10000)

    # Foreign Key Fields
    publisher = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)


class ScoreFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Score

    score = FuzzyChoice([1, 2, 3, 4, 5])
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

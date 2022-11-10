import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from apps.accounts.models import User
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
    publisher = factory.Iterator(User.objects.all())
    category = factory.Iterator(Category.objects.all())


class ScoreFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Score

    score = FuzzyChoice([1, 2, 3, 4, 5])
    user = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())

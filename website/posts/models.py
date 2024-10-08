from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Posts(models.Model):
    location = models.CharField(
        max_length=100,
        verbose_name='локация',
        help_text='здесь вы можете написать локацию'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата',
        help_text='дата создается автоматически'
    )
    category = models.CharField(
        max_length=50,
        verbose_name='категория',
        help_text='здесь вы можете написать категорию'
    )
    text = models.TextField(
        verbose_name='текст',
        help_text='здесь вы можете написать свой текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор',
        help_text='отображает имя автора'
    )
    groups = models.ForeignKey(
        'Groups',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группы',
        help_text='Здесь будут ваши группы'
    )


class Groups(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Здесь будет название вашей группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный адрес',
        help_text='Здесь будет уникальный адрес'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Здесь будет описание'
    )

    def __str__(self):
        return self.title

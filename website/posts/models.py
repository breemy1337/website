from django.db import models

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
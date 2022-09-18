from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название новости')
    content = models.TextField(blank=True, verbose_name='Новость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    categories = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')# null=True для того, чтобы что-то было указано для уже заведенных записей

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')# db_index - устанавливает индекс для удобного поиска
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
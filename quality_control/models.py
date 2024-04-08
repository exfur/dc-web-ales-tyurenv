from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('Новая', 'Новая'),
        ('В работе', 'В работе'),
        ('Завершена', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Высокий'),
        (4, 'Очень высокий'),
        (5, 'Критический'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bug_reports_as_project', verbose_name='Проект')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name='bug_reports_as_task', verbose_name='Задача')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новая', verbose_name='Статус')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3, verbose_name='Приоритет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баг-репорт'
        verbose_name_plural = 'Баг-репорты'


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Рассмотрение', 'Рассмотрение'),
        ('Принято', 'Принято'),
        ('Отклонено', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Высокий'),
        (4, 'Очень высокий'),
        (5, 'Критический'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название запроса на новую функцию')
    description = models.TextField(verbose_name='Описание запроса')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feature_requests', verbose_name='Проект')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name='feature_requests', verbose_name='Задача')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Рассмотрение', verbose_name='Статус запроса')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3, verbose_name='Приоритет запроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания запроса')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления запроса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрос на новую функцию'
        verbose_name_plural = 'Запросы на новые функции'
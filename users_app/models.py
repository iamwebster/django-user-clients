from django.db import models
from django.contrib.auth import get_user_model


STATUS_CHOICES = (
    ('Не в работе', 'Не в работе'),
    ('В работе', 'В работе'),
    ('Отказ', 'Отказ'),
    ('Сделка закрыта', 'Сделка закрыта'), 
)


class Client(models.Model):    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Список клиентов'
    
    account_number = models.PositiveIntegerField(verbose_name='Номер счета')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    middle_name = models.CharField(max_length=200, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='День рождения')
    inn = models.IntegerField(verbose_name='ИНН')
    responsible = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='Ответственный')
    status = models.CharField(max_length=100, default='Не в работе', choices=STATUS_CHOICES, verbose_name='Статус')


    def get_choices(self):
        choices = [choice[0] for choice in STATUS_CHOICES if self.status != choice[0]]
        return choices


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    

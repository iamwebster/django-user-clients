from django.db import models
from django.contrib.auth import get_user_model


class Client(models.Model):    
    account_number = models.PositiveIntegerField()
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    inn = models.IntegerField()
    responsible = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    status = models.CharField(max_length=100, default='Не в работе', choices=(
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    ))

    def __str__(self):
        return f'{self.last_name} {self.first_name} | {self.responsible.username}'

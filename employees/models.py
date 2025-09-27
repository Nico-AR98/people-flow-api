from django.db import models
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    surname = models.CharField(max_length=100, verbose_name=_('Surname'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('Email'))
    job_position = models.CharField(max_length=100, verbose_name=_('Job position'))
    salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Salary'))
    hire_date = models.DateField(verbose_name=_('Hire date'))

    def __str__(self):
        return f"{self.name} {self.surname}"

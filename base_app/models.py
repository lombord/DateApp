from django.db import models

# Create your models here.


class Profile(models.Model):
    STATUSES = [
        ('st', 'Studying'),
        ('wk', 'Working'),
        ('re', 'Retired'),
        ('ml', 'Millionaire'),
        ('no', 'Nothing'),
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUSES, default="no")
    salary = models.IntegerField()
    about = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

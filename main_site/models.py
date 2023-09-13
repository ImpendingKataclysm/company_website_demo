from django.db import models

MAX_FIELD_LEN = 80


class Employee(models.Model):
    """
    Database table for company employees whose profiles are displayed on the
    website.
    """
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    role = models.CharField(max_length=MAX_FIELD_LEN)
    image = models.ImageField(upload_to='employees')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}: {self.role}"

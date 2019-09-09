from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Students_Info'


class Contact(models.Model):
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'Contact_Me'




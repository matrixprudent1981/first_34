from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) # blank = True это необязательно в админ панели!
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}{self.title}'

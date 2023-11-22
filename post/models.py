from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True) # blank = True это необязательно в админ панели!
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}{self.title}'

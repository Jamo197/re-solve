from django.db import models
from django.db.models.deletion import CASCADE

from materials.models import Article


class Order(models.Model):
    price = models.PositiveIntegerField(default=0)
    # TODO: Implement if user drin 
    # customer = request_user_id

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Request(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=240, blank=True, null=True)
    # TODO: implement when user is implemented
    # request_user_id = User
    article = models.ForeignKey(Article, on_delete=CASCADE, related_name="requests")
    amount = models.PositiveIntegerField(default=1)
    # TODO: Implemnt Status Enum, wird von uns gesetzt, default=Enum irgendwas
    status = models.CharField(max_length=60, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.article.name
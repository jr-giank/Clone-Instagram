#Importaciones de Django
from django.contrib.auth.models import User
from django.db import models

#Importaciones locales
from users.models import Profile

class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} by @{self.user.username}'
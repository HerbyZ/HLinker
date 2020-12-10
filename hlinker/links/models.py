from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField('email', max_length=60, unique=True)
    username = models.CharField('username', max_length=30, unique=True)
    date_joined = models.DateTimeField('join date', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        app_label = 'links'


class Link(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.CharField('description', max_length=200)
    parent_link = models.URLField('parent link', max_length=5000)
    short_link = models.URLField('short link', max_length=20)
    follow_count = models.IntegerField('follow count', default=0)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    user = models.ForeignKey('links.User', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.name}: {self.short_link}'

    class Meta:
        app_label = 'links'

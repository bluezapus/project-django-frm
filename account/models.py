from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('please input your email active')
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
    
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=75)
    birthplace =models.CharField(max_length=150)
    birth = models.DateField(blank=True, default=timezone.now)
    email = models.EmailField(unique=True) #for username login must unique
    phone = models.IntegerField(blank=True, null=True)
    img_user = models.ImageField(blank=True, upload_to='users/', default='profile.png')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] #string parameter

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_lable):
        return True
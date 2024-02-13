from django.db import models
from django.urls import reverse
# Create your models here.
   
class Footer(models.Model):
    prehead=models.CharField(max_length=255)
    head=models.CharField(max_length=100)
    mid=models.CharField(max_length=50)
    pre=models.CharField(max_length=25)
    pri=models.CharField(max_length=20)
    end=models.CharField(max_length=19)
    
    def __str__(self):
        return self.prehead

class Price1(models.Model):
    kaz=models.CharField(max_length=255)
    rus=models.CharField(max_length=255)
    bagga=models.PositiveIntegerField(null = True)
    
    def __str__(self):
        return self.kaz
        
class Price2(models.Model):
    kaz=models.CharField(max_length=255)
    rus=models.CharField(max_length=255)
    bagga=models.PositiveIntegerField(null = True)
    
    def __str__(self):
        return self.kaz
    
class Price3(models.Model):
    kaz=models.CharField(max_length=255)
    rus=models.CharField(max_length=255)
    bagga=models.PositiveIntegerField(null = True)
    
    def __str__(self):
        return self.kaz

class Shop(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    about=models.TextField(blank=True)    
    
    def __str__(self):
        return self.title
    
class Reg(models.Model):
    esim = models.CharField(max_length=255, verbose_name="Esimi",default='') 
    teg=models.TextField(blank=True,default='', verbose_name="Tegi")
    nomer = models.IntegerField(verbose_name='Nomeri',default=87777777777)
    kala = models.CharField(max_length=255, verbose_name="Kalasy",default='') 
    email=models.EmailField(blank=True,default='@gmail.com',verbose_name='Elektrondyk poshta')
    image = models.ImageField(default='default value',upload_to='user_gallery', blank=True, null=True,verbose_name='3*4 suret')
    slug=models.SlugField(max_length=255,default='', unique=True, db_index=True, verbose_name="URL")
    is_published=models.BooleanField(default=True, verbose_name="Kelisim")

    REQUIRED_FIELDS = ['esim',]
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
      
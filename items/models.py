from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    cat_name = models.CharField(max_length=250,unique=True,default=1)
    slug=models.SlugField(max_length=250,unique=True,default=1)
    cat_spec=models.TextField()
    cat_image=models.ImageField(upload_to='category',blank=True)
    
    
    # class Meta:
    #     ordering=('cat_name',)
    #     verbose_name='categoryin'
    #     verbose_name_plural='hii'
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.cat_name)
        super().save(*args,**kwargs)
            
    
    def __str__(self):
        return '{}'.format(self.cat_name) 
class Products(models.Model):
    pro_name=models.CharField(max_length=200,unique=True,default=1)
    slug=models.SlugField(max_length=250,unique=True,default=1)
    pro_des=models.TextField(blank=True)
    pro_image=models.ImageField(upload_to='products',blank=True)
    pro_amount=models.DecimalField(max_digits=10,decimal_places=2,default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    stock=models.IntegerField(default=0)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.pro_name
    
    




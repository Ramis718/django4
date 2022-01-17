from django.db import models
from django.db.models.fields import TextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField()
    duration = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank = True, null=True)

    def cout_tag(self):
        return self.tag.filter(is_active=True).count()

    def review(self):
        c = 0
        for i in self.reviews.all():
            c += i.value
        try:    
            return c/self.reviews.all().count()
        except:
            return 0           

    
    def __str__(self):
        return f'{self.title}'

REW =(
    (1, 'good'),
    (2, 'sad'),
    (3, 'normal'),
    (4, 'very bad'),
    (5, 'very fine'),
)        



class Review(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(choices=REW)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text

from django.db import models

# Create your category  models here.

class Category(models.Model):
    title= models.CharField(max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title=models.CharField(max_length=100)
    # desc=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

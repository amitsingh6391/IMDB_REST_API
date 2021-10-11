from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

 #   ''' *** RELATIONSHIP IN DJANGO ****'''

    # '''Ther are three type of relationship in django
    # 1 One to one relationship 
    # 2 one to many relationship 
    # 3 many to many relationship '''


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about =models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title =models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title
    
   



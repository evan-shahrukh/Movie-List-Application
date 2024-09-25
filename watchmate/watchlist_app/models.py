from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name + " | " + str(self.website)
    

class WatchList(models.Model):
    title = models.CharField(max_length=200)
    story = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE,related_name="movies")
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title + " | " + str(self.created)

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=500,null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + "  ||  " + self.watchlist.title
    
from django.db import models

# Create your models here.
class Gallery(models.Model):
    image_id = models.IntegerField()
    image = models.ImageField()

    def return_image_id(self):
        return self.image_id
    
    def return_image(self):
        return self.image
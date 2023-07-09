from django.db import models

# Create your models here.


class fileupload(models.Model):
    Imagename = models.CharField(max_length=50)
    Imagefile = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.Imagename

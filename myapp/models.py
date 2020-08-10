from django.db import models
# Create your models here.
class Feedback(models.Model):
    First_Name = models.CharField(max_length = 250)
    Last_Name = models.CharField(max_length = 250)
    Email = models.EmailField(max_length = 250, unique=True)
    Contact_Number = models.CharField(max_length= 15,unique = True, null = False)
    Comment = models.TextField(max_length = 300)

    def __str__(self):
        return self.First_Name

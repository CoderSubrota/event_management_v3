from django.db import models
from event_management import settings
from django.contrib.auth.models import AbstractUser, Group, Permission



 
    
class Category_Model(models.Model):
    name = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Add_Event_Model(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    image = models.ImageField(max_length=5200,upload_to='event_images/', default='event_images/default.png')
   
    category = models.ForeignKey(
    Category_Model,  
    related_name="categories",
    on_delete=models.CASCADE
)

    def __str__(self):
        return self.name


class Create_Participant_Model(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True) 
    event_assign = models.ManyToManyField(Add_Event_Model, related_name="events")

    def __str__(self):
        return self.name


class RSVP_Model(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Add_Event_Model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
        

class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_images', blank=True, default='profile_images/default.jpg'
    )
    phone_number = models.TextField(blank=True)
    
    event_assign = models.ManyToManyField(
        Add_Event_Model, 
        related_name="participants", 
        blank=True
    )
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    def __str__(self):
        return self.username
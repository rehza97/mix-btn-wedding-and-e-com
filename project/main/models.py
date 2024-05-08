from django.db import models
from users.models import *
# Create your models here.
class Salle(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    nb_place = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    reduction = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True, null=True)
    localisation = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag= models.ManyToManyField("Tag", blank=True)
    Exta= models.ManyToManyField("ExtraServiceSalle", blank=True)
    image1= models.ImageField(upload_to='salles/') 
    image2= models.ImageField(upload_to='salles/',blank=True, null=True) 
    image3= models.ImageField(upload_to='salles/',blank=True, null=True) 
    image4= models.ImageField(upload_to='salles/',blank=True, null=True) 
    image5= models.ImageField(upload_to='salles/',blank=True, null=True) 
    facebook = models.CharField(max_length=250,blank=True, null=True) 
    
    def __str__(self):
        return self.title 

class ExtraServiceSalle(models.Model):
    title = models.CharField(max_length=250)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.title}  -prix {self.prix}'

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    reduction = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag= models.ManyToManyField("Tag", blank=True)
    GENDER_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    image1= models.ImageField(upload_to='produit/', blank=True, null=True) 
    image2= models.ImageField(upload_to='produit/', blank=True, null=True) 
    image3= models.ImageField(upload_to='produit/', blank=True, null=True) 
    image4= models.ImageField(upload_to='produit/', blank=True, null=True) 
    image5= models.ImageField(upload_to='produit/', blank=True, null=True) 
    
    def __str__(self):
        return self.title 
    
class CameraTeam(models.Model):
    banner = models.ImageField(upload_to="camera_team",blank=True , null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank = True , null = True)
    sex = [
        ('Homme', 'Homme'),
        ('Famme', 'Famme'),
        ('Les deux', 'Les deux'),
    ]
    pour = models.CharField(max_length=100, choices=sex,blank = True , null = True)
    drone = models.BooleanField(default=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title   

class ExtraService(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    reduction = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    banner = models.ImageField(upload_to="extraService/")  
    description = models.TextField(blank = True , null = True)
    def __str__(self) -> str:
        return self.titre
    
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, blank=True, null=True)
    photograph = models.ForeignKey(CameraTeam, on_delete=models.CASCADE, blank=True, null=True)
    extra_service = models.ForeignKey(ExtraService, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_validated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username} reserve {self.salle.title} from {self.start_date} to {self.end_date} '

class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
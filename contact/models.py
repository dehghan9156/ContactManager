from django.db import models



class Contact(models.Model):
    
    Gender_Choice = (
        ('woman','Woman'),
        ('man','Man'),
        ('unknown','Unknown')
    )
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    gender = models.CharField(max_length=10,choices=Gender_Choice,default='unknown')
    job = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
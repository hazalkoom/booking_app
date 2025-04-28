from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    image_url = models.TextField()  # This is base64 for now
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.property.name} by {self.user_name}"
from django.db import models


class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)


class addsuite(models.Model):
    NAME_CHOICES = [
        ('Executive Rooms (8500 INR)', 'Executive Rooms (8500 INR)'),
        ('Family Rooms(10500 INR)', 'Family Rooms(10500 INR)'),
        ('Pool Suite (11500 INR)', 'Pool Suite (11500 INR)'),
        # Add more choices as needed
    ]
        
    name=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=False,blank=False)
    phone=models.CharField(max_length=200)
    checkindate = models.DateField(null=True)
    checkintime=models.CharField(max_length=200,null=False,blank=True)
    checkoutdate=models.DateField(null=True)
    checkouttime=models.CharField(max_length=200,null=False,blank=True)
    
    roomtype=models.CharField(max_length=200,choices=NAME_CHOICES,null=True)
    #roomtype=models.IntegerField(null=True)

    def __str__(self):
        return self.name


class addtable(models.Model):
    
    name=models.CharField(max_length=200,null=False,blank=False)
    contact=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=False,blank=False)
    #venue=models.TextChoices(null=True)
    nooftables=models.CharField(max_length=200,null=True,blank=False)
    date=models.DateField(null=True)
    time=models.CharField(max_length=200,null=True,blank=False)
    message=models.CharField(max_length=200,null=True,blank=False)
    
    def __str__(self):
        return self.name


class addvenue(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    contact=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    #venue=models.CharField(max_length=200,null=False,blank=False)
    checkindate = models.DateField(null=True)
    checkoutdate = models.DateField(null=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()
    def __str__(self) :
        return f'Message from {self.name}'

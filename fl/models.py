from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    Size = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    tube_diameter = models.CharField(max_length=50,default=None)
    maximum_height = models.CharField(max_length=50,default=None)
    base = models.CharField(max_length=50,default=None)
    color = models.CharField(max_length=50,default=None)
    Capacity = models.CharField(max_length=50)
    Material = models.CharField(max_length=100)
    Non_slip_legs = models.CharField(max_length=5)
    category = models.CharField(max_length=100)
    LastScrappeddate = models.DateTimeField(auto_now=True)
    Updateddate = models.DateTimeField(auto_now=True)
    Createddate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50)
    main_image_url = models.CharField(max_length=255)
    class Meta:
        db_table = 'product'

class Image(models.Model):
    image_url = models.CharField(max_length=255, primary_key=True)
    sku = models.CharField(max_length=50)

    # Define the ForeignKey relationship
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


from django.db import models


class Crops(models.Model):
    cid=models.CharField(max_length=20,default=1)
    name=models.CharField(max_length=20)
    variety=models.CharField(max_length=20)
    planting_date=models.DateField()
    description=models.TextField()
    quantity=models.IntegerField()
    is_harvested=models.BooleanField(default=False)

    class Meta:
        db_table="crops"


# Animals model

class Animals(models.Model):
    Aid=models.CharField(max_length=1000000, default=0)
    picture=models.ImageField(upload_to='animal_pictures')
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    production=models.DecimalField(decimal_places=2, max_digits=3)




    #Machinery model

class Machinery(models.Model):
        
        number_plate=models.CharField(max_length=20, primary_key=True)
        model=models.CharField(max_length=20)
        purchase_date=models.DateField()
        description=models.TextField()
        manufacture_year=models.IntegerField()
        purchase_price=models.DecimalField(decimal_places=2, max_digits=30)

        class Meta:
            db_table="machinery"



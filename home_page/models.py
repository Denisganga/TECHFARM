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


            #expense model

class Expenses(models.Model):
     
     Eid=models.IntegerField(default=1,primary_key=True)
     date=models.DateField()
     description=models.TextField()
     amount=models.BigIntegerField()
     receipt = models.FileField(upload_to='expenses/', blank=True, null=True)

     class Meta:
          db_table="expense"

          #reports model



class Reports(models.Model):
     
     Rid=models.IntegerField(default=1,primary_key=True)
     date=models.DateField()
     the_field=models.TextField()
     the_report=models.TextField()
     
class Overview(models.Model):
     
     Fid=models.IntegerField(default=1,primary_key=True)
     Assets=models.CharField(max_length=100000)
     Number=models.TextField()

     class Meta:
          db_table="farm_overview"


class Employees(models.Model):
     Eid=models.IntegerField(default=1,primary_key=True)
     Name=models.CharField(max_length=20)
     Position=models.CharField(max_length=20)
     Salary=models.IntegerField()
     Performance=models.CharField(max_length=20)


     class Meta:
          db_table="emloyees"

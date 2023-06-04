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



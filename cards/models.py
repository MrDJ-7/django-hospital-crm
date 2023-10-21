from django.db import models


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=25)


class Cards(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    date_created = models.IntegerField()
    date_updated = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "Card"

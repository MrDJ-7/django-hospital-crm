from django.db import models


class Doctors(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField("date published")

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = "Doctors"


# list = Doctor.objects.filter("name", Name)

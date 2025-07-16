from django.db import models

# Create your models here.

AGE_GROUPS = [
    ('U1', 'Under 1 Year'),
    ('U5', 'Under 5 Years'),
    ('A5', 'Above 5 Years'),
]

class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PatientCount(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    date = models.DateField()
    age_group = models.CharField(max_length=2, choices=AGE_GROUPS)
    male = models.PositiveIntegerField(default=0)
    female = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['disease', 'date', 'age_group']

    def total(self):
        return self.male + self.female

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emplyee_regNo = models.TextField(unique=True)
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class categoria(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre =models.CharField(max_length=100)
    class Meta:
        db_table="categoriatabla"
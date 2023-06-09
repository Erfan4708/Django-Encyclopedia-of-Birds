
# Create your models here.
from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    parent_group = models.CharField(max_length=100)
    height = models.FloatField()
    lifespan = models.IntegerField()


class Species(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)


class Domain(models.Model):
    name = models.CharField(max_length=100)


class Kingdom(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)


class Phylum(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)


class Class(models.Model):
    name = models.CharField(max_length=100)
    phylum = models.ForeignKey(Kingdom, on_delete=models.CASCADE)


class Order(models.Model):
    name = models.CharField(max_length=100)
    Class = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

class Family(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Kingdom, on_delete=models.CASCADE)


class Genus(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Kingdom, on_delete=models.CASCADE)


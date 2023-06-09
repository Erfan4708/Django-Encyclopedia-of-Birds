# Create your models here.
from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    parent_group = models.CharField(max_length=100)
    height = models.FloatField()
    lifespan = models.IntegerField()

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kingdom(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Phylum(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    phylum = models.ForeignKey(Phylum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Species(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal.name

# Create your models here.
from django.db import models
from django.urls import reverse


class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Kingdom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Phylum(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phylum = models.ForeignKey(Phylum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Species(models.Model):
    # animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight = models.FloatField()
    parent_group = models.CharField(max_length=100)
    height = models.FloatField()
    lifespan = models.IntegerField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('bird_detail', args=[self.id])

    def __str__(self):
        return self.name

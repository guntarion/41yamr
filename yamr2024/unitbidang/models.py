from django.db import models

class Bidang(models.Model):
    namaBidang = models.CharField(max_length=200)
    kodeBidang = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.namaBidang


class Unit(models.Model):
    namaUnit = models.CharField(max_length=200)
    kodeUnit = models.CharField(max_length=10)
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)

    def __str__(self):
        return self.kodeUnit + ' ' + self.namaUnit

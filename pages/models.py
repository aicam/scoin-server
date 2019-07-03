from django.db import models
from django.utils import timezone


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)


class advertisement(models.Model):
    advertisement_id = models.IntegerField(max_length=10, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    short_description = models.CharField(max_length=250)
    time = models.DateTimeField(default=one_day_hence())
    minlevel = models.IntegerField(max_length=3)
    old_cost = models.IntegerField(default=100)
    off = models.IntegerField(default=10)
    cost = models.IntegerField(max_length=10)
    link = models.CharField(max_length=50)
    pic_link = models.CharField(max_length=200)
    rate = models.FloatField(max_length=2)
    rate_count = models.IntegerField(max_length=10)
    bought = models.IntegerField(default=200)
    longitude = models.FloatField(max_length=10)
    latitude = models.FloatField(max_length=10)
    Scoin_available = models.IntegerField(default=0)
    Scoin_cost = models.IntegerField(default=20)
    priority = models.IntegerField(max_length=3)


class Users(models.Model):
    userID = models.IntegerField(max_length=10, primary_key=True)
    username = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=15)
    sex = models.BooleanField(max_length=1)
    level = models.IntegerField(max_length=3)
    Scoin = models.FloatField(max_length=10)
    level_grow = models.FloatField(max_length=3)
    notifications = models.IntegerField(default=0)


class Users_Payment(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey('advertisement', on_delete=models.CASCADE)
    cost = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=1)


class Comments(models.Model):
    ad = models.ForeignKey('advertisement', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    comment = models.CharField(max_length=30)


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class ADCategory(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    ad = models.ForeignKey('advertisement', on_delete=models.CASCADE)


class dailySuggestions(models.Model):
    id = models.IntegerField(primary_key=True)
    ad = models.ForeignKey('advertisement', on_delete=models.CASCADE)
    active = models.IntegerField()

class AD_pics(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.ForeignKey('advertisement',on_delete=models.CASCADE,default=1)
    pic_link = models.CharField(max_length=200)

class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=50)


class Game_rates(models.Model):
    game = models.ForeignKey('Games', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    rate = models.IntegerField()

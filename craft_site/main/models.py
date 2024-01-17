from django.db import models
#python manage.py makemigrations та python manage.py migrate

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    trip_from = models.CharField(max_length=200)
    trip_to = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    data = models.DateField(verbose_name="data of trip")
    phone = models.IntegerField(default=0, null=False, blank=False, verbose_name='Client phone number')
    count_of_passengers = models.IntegerField(default=0, null=False, blank=False, verbose_name='Count of passengers')
    desc = models.CharField(max_length=200, default=0, null=True)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.trip_from, self.trip_to, self.day, self.data, self.phone, self.count_of_passengers, self.desc


class Routes(models.Model):
    cities_list = models.CharField(max_length=200)
    price = models.IntegerField(default=0, null=False, blank=False)
    day_start = models.CharField(max_length=200)
    day_finish = models.CharField(max_length=200)
    time_start = models.CharField(max_length=200)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cities_list, self.price, self.day_start, self.day_finish, self.time_start


class Cars(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=0, null=False, blank=False)
    photos = models.ImageField(upload_to='car_photos/')
    information = models.CharField(max_length=200)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.year, self.information


class Driver(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0, null=False, blank=False)
    photo = models.ImageField(upload_to='driver_photos/')
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.age


class Response(models.Model):
    name = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    registration_time = models.DateTimeField(auto_now_add=True)


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

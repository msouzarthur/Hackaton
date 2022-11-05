from django.db import models

# Create your models here.
class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    route_name = models.CharField(max_length=100)
    route_est_time = models.TimeField()
    route_time = models.TimeField()

class Stop(models.Model):
    stop_id = models.IntegerField(primary_key=True)
    stop_name = models.CharField(max_length=100)
    stop_lat = models.DecimalField(max_digits=9, decimal_places=6)
    stop_lon = models.DecimalField(max_digits=9, decimal_places=6)
    stop_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    def __str__(self):
        return self.stop_name

class RouteStop(models.Model):
    stop_id = models.ForeignKey(Stop, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_order = models.IntegerField()

class Passenger(models.Model):
    passenger_lat = models.DecimalField(max_digits=9, decimal_places=6)
    passenger_lon = models.DecimalField(max_digits=9, decimal_places=6)
    passenger_route = models.ForeignKey(Route, on_delete=models.CASCADE)

class Student(Passenger):
    student_id = models.IntegerField(primary_key=True)
    student_rank = models.IntegerField(primary_key=True, max_length=10)

class Driver(Passenger):
    driver_id = models.CharField(primary_key=True, max_length=10)
    driver_name = models.CharField(max_length=50)

class Bus(models.Model):
    bus_id = models.CharField(max_length=10)
    bus_lat = models.DecimalField(max_digits=9, decimal_places=6)
    bus_long = models.DecimalField(max_digits=9, decimal_places=6)
    bus_speed = models.DecimalField(max_digits=9, decimal_places=6)
    bus_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus_time = models.TimeField()
    bus_occupation = models.IntegerField()
    bus_capacity = models.IntegerField()
    bus_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.bus_id
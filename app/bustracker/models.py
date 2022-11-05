from django.db import models

class Route(models.Model):
    route_name = models.CharField(max_length=100)
    route_est_time = models.TimeField()
    route_time = models.TimeField()

class Stop(models.Model):
    stop_name = models.CharField(max_length=100)
    stop_lat = models.DecimalField(max_digits=9, decimal_places=7)
    stop_lon = models.DecimalField(max_digits=9, decimal_places=7)
     
    def __str__(self):
        return self.stop_name


class Passenger(models.Model):
    class Meta:
        abstract = True
    passenger_lat = models.DecimalField(max_digits=9, decimal_places=7)
    passenger_lon = models.DecimalField(max_digits=9, decimal_places=7)
    passenger_route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)

class Student(Passenger):
    student_rank = models.IntegerField()

class Driver(Passenger):
    driver_name = models.CharField(max_length=50)

class Bus(models.Model):
    bus_plate = models.CharField(max_length=10)
    bus_lat = models.DecimalField(max_digits=9, decimal_places=7)
    bus_long = models.DecimalField(max_digits=9, decimal_places=7)
    bus_speed = models.DecimalField(max_digits=9, decimal_places=6)
    bus_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus_occupation = models.IntegerField()
    bus_capacity = models.IntegerField()
    bus_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.bus_id

    def get_location(self):
        return self.bus_lat, self.bus_long
    
    def get_speed(self):
        return self.bus_speed
    
    def get_occupation(self):
        return self.bus_occupation
    
    def get_capacity(self):
        return self.bus_capacity
    

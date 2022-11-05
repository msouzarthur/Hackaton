from django.db import models

class Route(models.Model):
    route_name = models.CharField(max_length=100)
    route_est_time = models.TimeField()
    route_time = models.TimeField()

class Stop(models.Model):
    stop_name = models.CharField(max_length=100)
    stop_lat = models.DecimalField(max_digits=9, decimal_places=7)
    stop_lon = models.DecimalField(max_digits=9, decimal_places=7)
    stop_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.stop_name

class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_order = models.IntegerField()
   
    def __str__(self):
        return self.route.route_name + ' ' + self.stop.stop_name

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

    def get_location(self):
        return self.bus_lat, self.bus_long
    
    def get_speed(self):
        return self.bus_speed
    
    def get_occupation(self):
        return self.bus_occupation
    
    def get_capacity(self):
        return self.bus_capacity
    
    def describe(self):
        return self.bus_plate + ' ' + self.bus_route.route_name + ' ' + self.bus_driver.driver_name + ' ' + self.bus_occupation + ' ' + self.bus_capacity

class Reservation(models.Model):
    reservation_passenger = models.ForeignKey(Student, on_delete=models.CASCADE)
    reservation_bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    reservation_start = models.ForeignKey(RouteStop, on_delete=models.CASCADE)
    reservation_end = models.ForeignKey(RouteStop, on_delete=models.CASCADE, related_name='reservation_end')
    reservation_time = models.TimeField()

    def __str__(self):
        return self.reservation_id

    def get_date(self):
        return self.reservation_date

    def get_time(self):
        return self.reservation_time

    def describe(self):
        return self.reservation_passenger + ' ' + self.reservation_bus + ' ' + self.reservation_start + ' ' + self.reservation_end + ' ' + self.reservation_time
    

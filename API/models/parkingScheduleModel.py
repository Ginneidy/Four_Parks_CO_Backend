from django.db import models
from API.models.parkingModel import Parking
from API.models.scheduleModel import Schedule

class ParkingSchedule(models.Model):
    parking = models.OneToOneField(Parking, models.DO_NOTHING, primary_key=True)  # The composite primary key (parking_id, schedule_id) found, that is not supported. The first column is selected.
    schedule = models.ForeignKey(Schedule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parking_schedule'
        unique_together = (('parking', 'schedule'),)
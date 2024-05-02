from django.db import models
from API.models.feeModel import Fee
from API.models.parkingModel import Parking

class ParkingFee(models.Model):
    fee = models.OneToOneField(Fee, models.DO_NOTHING, primary_key=True)  # The composite primary key (fee_id, parking_id) found, that is not supported. The first column is selected.
    parking = models.ForeignKey(Parking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parking_fee'
        unique_together = (('fee', 'parking'),)
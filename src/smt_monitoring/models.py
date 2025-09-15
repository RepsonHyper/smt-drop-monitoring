from django.core.validators import MinValueValidator
from django.db import models

class Event(models.Model):
    timestamp = models.DateTimeField()
    lane = models.SmallIntegerField()
    mc = models.CharField(max_length=10)
    fadd = models.IntegerField()
    fsadd = models.SmallIntegerField()
    pn = models.CharField(max_length=20)
    feeder_serial = models.CharField(max_length=30, null=True, blank=True)
    pickup = models.IntegerField(validators=[MinValueValidator(0)])
    pmiss = models.IntegerField(validators=[MinValueValidator(0)])
    rmiss = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "lane", "mc", "fadd", "fsadd", "pn"],
                name="unique_event_key"
            )
        ]
        indexes = [
            models.Index(fields=["timestamp", "lane", "mc"]),
            models.Index(fields=["pn"]),
        ]

    def __str__(self):
        return f"{self.timestamp} |Lane: {self.lane} | Slot: {self.fadd}.{self.fsadd} | Part: {self.pn}"

from django.db import models

class WgUser(models.Model):
    serial_number = models.IntegerField(unique=True)
    public_key = models.CharField(max_length=44)
    private_key = models.CharField(max_length=44, default='your private key')
    expire_date = models.DateField()
    # it can be the user's real name
    alias = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.serial_number) + self.alias


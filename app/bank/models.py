from django.db import models

class Branch (models.Model):
    branch_name = models.CharField(max_length=50)
    location_city = models.CharField(max_length=50)
    location_id = models.CharField(max_length=20)

    def __str__ (self):
        return (
            f"Bank Name : {self.branch_name} | Branch Name : {self.location_city}"
        )

    class Meta:
        verbose_name_plural = "Branches"


class Client (models.Model):
    client_name = models.CharField(max_length=50, default="")
    client_email = models.EmailField(max_length=200, default="")

    branch_connection =  models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
        )   

    def __str__ (self):
        return (
            f"{self.client_name} | {self.branch_connection}" 
        )

class Account(models.Model):
    checking_balance = models.FloatField(max_length=500, default=0)
    # checking_balance = models.FloatField(max_length=500)
    client_connection = models.OneToOneField(
        Client,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return(
            f"{self.client_connection.client_name} | Checking Balance :{self.checking_balance}"
        )



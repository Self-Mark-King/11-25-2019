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
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=200)

    branch models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
        )   

    def __str__ (self):
        return (
            f"{self.client_name} | {self.branch}" 
        )

class Account(models.Model):
    has_checking = models.BooleanField
    has_savings = models.BooleanField
    checking_balance = models.FloatField(max_length=500)
    checking_balance = =models.FloatField(max_length=500)
    client = models.OneToOneField(
        client,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return(
            f"{self.client.client_name} | Checking Balance :
            {self.checking_balance} | Savings Balance :
            {self.savings_balance}"
        )



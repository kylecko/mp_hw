from django.db import models

# Create your models here.

class File(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    client_member_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone_number} {self.client_member_id} {self.account_id}'

class Provider(models.Model):
    company = models.CharField(max_length=50)
    client_member_id = models.ForeignKey(File, on_delete=models.CASCADE, related_name='unique_cm_id')
    phone_number = models.ForeignKey(File, on_delete=models.CASCADE, related_name='unique_ph')
    
    def __str__(self):
        return f'{self.company} {self.client_member_id} {self.phone_number}'


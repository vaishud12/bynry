from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.service_type} - {self.status}"

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True)

    def __str__(self):
        return self.user.username

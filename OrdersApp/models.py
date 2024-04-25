from django.db import models
from django.contrib.auth.models import AbstractUser
from CustomersApp.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    auth_token = models.CharField(max_length=255, blank=True, null=True)

    # Specify custom related_name arguments
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set", # Custom related_name
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_set", # Custom related_name
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username
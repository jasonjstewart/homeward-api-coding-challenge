from django.db import models

### Current Customer Model
# - Name
# - Email
# - Phone number
# - Current address (text field)
class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    current_address = models.CharField(max_length=100)
    brokerage_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    current_address = models.CharField(max_length=100)

# Create your models here.
### Current Application Model
# - Customer
# - Purchasing address (text field)
# - Application approved (boolean)
# - Agent name

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    purchasing_address = models.CharField(max_length=100)
    application_approved = models.BooleanField(default=False)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL)



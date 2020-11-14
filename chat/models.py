from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="messages" ,on_delete=models.CASCADE)
    polarity=models.CharField(max_length=255,default=0)
    subjectivity=models.CharField(max_length=255,default=0)
    def __str__(self):
        return self.message+self.polarity+self.subjectivity

class Patient(models.Model):

    pat_id=models.IntegerField(primary_key=True)
    CATEGORY = [('W', 'Worst'),
                    ('G', 'Good'),
                    ('B', 'Better- Slowly Recovering'),
                    ('V', 'Vulnerable')]
    CARE=[('I','Intensive Care'),('B','Behavioural Care'),('P','Palliative Care'),('O','Ordinary Care'),('S','Special Care')]
    name = models.CharField(max_length=200)
    First_name=models.CharField(default="",max_length=200)
    Second_name=models.CharField(default="",max_length=200)
    current_location=models.CharField(default="",max_length=200)
    nationality=models.CharField(default="",max_length=200)
    pin_code=models.CharField(default="",max_length=200)
    #user = models.ForeignKey(User, related_name="patient", on_delete=models.CASCADE)
    email_address = models.EmailField(default="")
    criticality_level=models.IntegerField(default=3)
    e_y_s=models.IntegerField(default=90)
    n_y_c=models.IntegerField(default=10)
    education=models.CharField(default='University of WIndsor',max_length=200)
    profession=models.CharField(default='Business Executive',max_length=200)
    few_words=models.CharField(default='Enthusiastic Gamer often iek to defeat others while playing multiplayer_game',max_length=2000)
    category = models.CharField(choices=CATEGORY, max_length=300, default="")
    age=models.IntegerField()
    address=models.CharField(max_length=1000)
    severity=models.CharField(max_length=1000)
    issues=models.CharField(max_length=1000)
    date_admitted=models.DateField()
    care_provided=models.CharField(choices=CARE,default="",max_length=1000)
    care_needed=models.CharField(max_length=1000)
    health_level=models.CharField(max_length=1000)
    sex=models.CharField(max_length=1000)
    cp=models.CharField(max_length=1000)
    trestbps=models.CharField(max_length=1000)
    chol=models.CharField(max_length=1000)
    fbs=models.CharField(max_length=1000)
    restecg=models.CharField(max_length=1000)
    thalach=models.CharField(max_length=1000)
    exang=models.CharField(max_length=1000)
    oldpeak=models.CharField(max_length=1000)
    slope=models.CharField(max_length=1000)
    ca=models.CharField(max_length=1000)
    thal=models.CharField(max_length=1000)
    def __str__self(self):
        return self.pat_id

class Volunteer(models.Model):
    vol_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
   # user = models.ForeignKey(User, related_name="volunteer", on_delete=models.CASCADE)
    age = models.IntegerField()
    volunteering_experience=models.IntegerField(default=10)
    operations_handled=models.IntegerField(default=10)
    patients_helped=models.IntegerField(default=10)
    First_name = models.CharField(default="", max_length=200)
    Second_name = models.CharField(default="", max_length=200)
    current_location = models.CharField(default="", max_length=200)
    nationality = models.CharField(default="", max_length=200)
    pin_code = models.CharField(default="", max_length=200)
    education = models.CharField(default='University of WIndsor', max_length=200)
    profession = models.CharField(default='Business Executive', max_length=200)
    few_words = models.CharField(default='Enthusiastic Gamer often iek to defeat others while playing multiplayer_game',
                                 max_length=2000)
    email_address=models.EmailField(default="",max_length=500)
  #  category = models.CharField(choices=CATEGORY, max_length=300, default="")
    proof=models.CharField(max_length=200)
    lisences_hold=models.CharField(max_length=200)
    verfication_status=models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    available_date=models.DateField()
    services=models.CharField(max_length=1000)
class Nurse(models.Model):
    #user = models.ForeignKey(User, related_name="nurse", on_delete=models.CASCADE)
    nurse_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    First_name = models.CharField(default="", max_length=200)
    Second_name = models.CharField(default="", max_length=200)
    current_location = models.CharField(default="", max_length=200)
    nationality = models.CharField(default="", max_length=200)
    pin_code = models.CharField(default="", max_length=200)
    email_address=models.EmailField(max_length=254)
    mobile_number=models.IntegerField()
    operations_handled=models.IntegerField(default=10)
    few_words = models.CharField(default='Enthusiastic Gamer often iek to defeat others while playing multiplayer_game',
                                 max_length=2000)
    patients_handled=models.IntegerField(default=10)
    age=models.IntegerField()
    about_me=models.CharField(max_length=1000)
    years_of_experience=models.DecimalField(decimal_places=2,max_digits=10)
    address=models.CharField(max_length=1000)
    specialisation=models.CharField(max_length=200)
    education=models.CharField(max_length=2000)
    complex_cases_handled=models.CharField(max_length=2000)
    availability=models.DateTimeField()
class health_habbits(models.Model):
    classofpatients=[('A','Good'),('B','Historical Complications'),('C', 'Disaster due to unexpected situations')]
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    hid=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Life_expectancy=models.IntegerField(default=10)
    Alcohol_percentage=models.IntegerField(default=10)
    expenditure_income=models.IntegerField(default=10)
    STIs=models.BooleanField(choices=TRUE_FALSE_CHOICES)
    BMI=models.IntegerField(default=10)
    Polio=models.BooleanField(choices=TRUE_FALSE_CHOICES)
    Total_expenditure=models.IntegerField(default=10)
    Class=models.CharField(choices=classofpatients,default="",max_length=300)
    Adult_smoking=models.BooleanField(choices=TRUE_FALSE_CHOICES)
    Physical_inactivity=models.BooleanField(choices=TRUE_FALSE_CHOICES)


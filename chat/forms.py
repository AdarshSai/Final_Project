from django import forms
from .models import Patient, Volunteer, Nurse


class PatientRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Patient
        fields = ['pat_id', 'name','First_name','Second_name','current_location','nationality','pin_code','email_address','criticality_level','e_y_s' ,'n_y_c','education','profession','few_words','category' ,'age','address','severity','issues','date_admitted','care_provided','care_needed','health_level','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']


class VolunteerRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Volunteer
        fields =['vol_id', 'name', 'age', 'volunteering_experience','operations_handled', 'patients_helped', 'First_name', 'Second_name', 'current_location', 'nationality', 'pin_code', 'education', 'profession', 'few_words', 'email_address', 'proof', 'lisences_hold', 'verfication_status', 'address','available_date', 'services' ]

class NurseRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Nurse
        fields=['nurse_id','user_name','name','First_name','Second_name','current_location','nationality','pin_code', 'email_address','mobile_number','operations_handled','few_words','patients_handled','age','about_me','years_of_experience','address','specialisation','education','complex_cases_handled','availability']
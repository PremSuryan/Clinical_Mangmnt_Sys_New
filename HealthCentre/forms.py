from django.forms import ModelForm
from .models import Appointment, Medicine, Patient
from django import forms
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class AppointmentSet(forms.Form):
    # my_date_field = forms.DateField(widget=DatePickerInput)
    # my_time_field = forms.TimeField(widget=TimePickerInput)
    my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)

class AppointmentSetForm(ModelForm):
    class Meta:
        model = Appointment
        
        fields = ['subject', 'time', 'notes']

        widgets = {
            'time' : DateTimePickerInput(),
            
        }

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

class PatientMedicineForm(ModelForm):
    class Meta:
        model = Medicine
        model = Patient
        
        fields = ['medicinename' , 'beforeafter']
        fields = ['name' , 'address' , 'contactNumber' , 'email' , 'rollNumber' , 'passwordHash']

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email')

class VerifyOTPForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=6)

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError("The new passwords don't match.")
        
        
# class TimeInput(forms.TimeInput, forms.DateInput):
#     timeInputType = 'time'
#     dateinputType = 'date'

# class AppointmentForm(ModelForm):
    # hour = forms.TimeField(widget=forms.Select(choices=[
    #     (hour, hour) for hour in range(0, 24)   
    # ]))
    # min = forms.TimeField(widget=forms.Select(choices=[
    #     (min, min) for min in range(0, 60)
    # ]))

    # class Meta:
    #     model = Appointment
    #     fields = ['time', 'date']
    #     widgets = {
    #         'time': TimeInput(),
    #     }
    #     # field_classes = {
    #     #     'time': 'form-control col-md-6',
    #     #     'min': 'form-control col-md-6',
    #     # }
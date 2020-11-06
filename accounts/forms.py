from django import forms
from .models import users,doctor,Disease,FamilyDisease,patient


class user_sign(forms.ModelForm):
    class Meta:
        model   = users
        fields  = '__all__'
        exclude = ("joined_at","is_active","is_admin","is_staff","is_superuser","user_type","last_login","slug","password",)



class doctor_sign(forms.ModelForm):
    class Meta:
        model   = doctor
        fields  = '__all__'
        exclude = ("user","start","end",)



class patient_sign(forms.ModelForm):
    class Meta:
        model   = patient
        fields  = '__all__'
        exclude = ("user",)

class dieseas(forms.ModelForm):
    class Meta:
        model   = Disease
        fields  = '__all__'
        exclude = ("patient",)


class f_dieseas(forms.ModelForm):
    class Meta:
        model   = Disease
        fields  = '__all__'
        exclude = ("patient",)
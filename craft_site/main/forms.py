from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)


class AddNewBooking(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    trip_from = forms.CharField(label="City where trip start", max_length=200)
    trip_to = forms.CharField(label="City where trip finish", max_length=200)
    day = forms.CharField(label="Vivtorok, chetver, patnutsa, nedila", max_length=200)
    data = forms.DateField(label="data of trip")
    phone = forms.IntegerField(label="mobile phone")
    count_of_passengers = forms.IntegerField(label="count of passengers")
    desc = forms.CharField(label="desc of trip")

from django import forms

class BookRoomForm(forms.Form):
    room_id = forms.IntegerField(widget=forms.HiddenInput)

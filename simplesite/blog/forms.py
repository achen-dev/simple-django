from django import forms


class NumberForm(forms.Form):

    number = forms.IntegerField(
        max_value=100,
        min_value=0,
        help_text="Please enter an integer",
        required=True
    )


class MLForm(forms.Form):
    image = forms.FileField(
        help_text="Please upload an image in .jpg format and is less than 5 Megabytes",
    )



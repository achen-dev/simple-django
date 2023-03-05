from django import forms


class BasicForm(forms.Form):

    number = forms.IntegerField(
        max_value=100,
        min_value=0,
        help_text="Please enter an integer",
        required=True
    )



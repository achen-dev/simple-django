from django import forms


class NumberForm(forms.Form):

    number = forms.IntegerField(
        max_value=100,
        min_value=0,
        help_text="Please enter an integer",
        required=True
    )


class MLForm(forms.Form):

    age = forms.IntegerField(
        max_value=200,
        min_value=0,
        help_text="Please enter your age"
    )
    cabin = forms.CharField(
        help_text="Please enter your desired cabin"
    )



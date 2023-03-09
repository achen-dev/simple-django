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
        label="Your age when boarding the titanic",
        max_value=200,
        min_value=0,
        help_text="Please enter your age",
        initial="0"
    )
    cabin = forms.CharField(
        help_text="Please enter your desired cabin"
    )

    file = forms.FileField()



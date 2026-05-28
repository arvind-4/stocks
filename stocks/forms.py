"""Form definitions for the stocks app."""

from django import forms


class StocksForm(forms.Form):
    """Form for entering a stock ticker symbol."""

    name = forms.CharField(
        label="",
        max_length=120,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter a Stock Name", "class": "form-control"}
        ),
    )

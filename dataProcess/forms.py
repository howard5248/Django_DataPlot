from django import forms
from tempus_dominus.widgets import DatePicker

class DatePickForm(forms.Form):
    date_field1 = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '2012-01-01',
                'maxDate': '2019-12-31',
            },
        ),
        initial='2016-01-01',
        label='起始時間'
    )
    date_field2 = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '2012-01-01',
                'maxDate': '2019-12-31',
            },
        ),
        initial='2016-01-31',
        label='結束時間'
    )
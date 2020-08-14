from django import forms
from .models import TimetableEntry
from . import models as timetable_model



class TimetableEntry_form(forms.ModelForm):


    class Meta:
        model = TimetableEntry
        exclude = ('week',)

    def __init__(self, *args, **kwargs):
        super(TimetableEntry_form, self).__init__(*args, **kwargs)
        self.fields['custom_begins'].widget.attrs['class'] = 'custom_time'
        self.fields['custom_ends'].widget.attrs['class'] = 'custom_time'
        self.fields['isCustom_time'].widget.attrs['id'] = 'is_custom_btn'


class WeeksSelection_form(forms.Form):
    weeks = forms.MultipleChoiceField(choices=timetable_model.WEEKS,
                                      widget=forms.CheckboxSelectMultiple,
                                      )

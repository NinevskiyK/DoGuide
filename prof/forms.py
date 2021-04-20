from django import forms
from search.models import Excursion
from lk.models import Profile


class ExcursionForm(forms.ModelForm):

    class Meta:
        model = Excursion
        fields = ('Place', 'Img', 'Description', 'Max_number', 'Cost', 'Time', 'Place', 'City', 'Country',
                  'Short_description')

    def __init__(self, *args, **kwargs):
        super(ExcursionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def as_table(self):
        return self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s    </th><td>%(errors)s%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<small id="id_username" class="form-text text-muted">%s</small>',
            errors_on_separate_row=False)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'Img')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def as_table(self):
        return self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s    </th><td>%(errors)s%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<small id="id_username" class="form-text text-muted">%s</small>',
            errors_on_separate_row=False)
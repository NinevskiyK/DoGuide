from django import forms
from search.models import Excursion, Book


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
        return html


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('vk', 'data')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def as_table(self):
        return self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s    </th><td>%(errors)s%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<small id="id_username" class="form-text text-muted">%s</small>',
            errors_on_separate_row=False)
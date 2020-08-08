from django import forms

from ..models import Farm


class BaseFarmFormMixin(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'


class NewFarmForm(BaseFarmFormMixin):
    """Do nothings"""


class EditFarmForm(BaseFarmFormMixin):
    class Meta(BaseFarmFormMixin.Meta):
        exclude = ['id', 'slug']

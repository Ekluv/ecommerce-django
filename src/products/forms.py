from django import forms

import models


class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = models.Variation
		fields = ('title', 'price', 'sale_price', 'inventory', 'active')


VariationInventoryFormSet = forms.models.modelformset_factory(models.Variation, form=VariationInventoryForm, extra=1)
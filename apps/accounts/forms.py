from django import forms

from apps.accounts.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)

        # filter these two query sets for avoiding self follow
        if self.instance:
            self.fields['follower'].queryset = self._meta.model.objects.prevent_self_reference(self.instance.id)
            self.fields['following'].queryset = self._meta.model.objects.prevent_self_reference(self.instance.id)

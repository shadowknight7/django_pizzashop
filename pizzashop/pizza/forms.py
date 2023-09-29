from django import forms
from.models import Pizza

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='topping1',max_length=50,widget=forms.Textarea)
#     topping2 = forms.CharField(label='topping2', max_length=50,widget=forms.PasswordInput)
#     size = forms.ChoiceField(label='size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
#         # labels = {'topping1':'t1','topping2':'t2'}  #to change the label name
#         widgets = {'topping1':forms.Textarea,'topping2':forms.PasswordInput}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=1,max_value=10)
from django import forms
from .models import SociosSuscriptoresModel, ContactoModel

class DateInput(forms.DateInput):
    input_type = 'date'

class SociosSuscriptoresForm(forms.ModelForm):
    
    
    class Meta:
        model = SociosSuscriptoresModel
        fields = '__all__'
        widgets = {
            'nacimiento': DateInput()
        }


    def __init__(self, *args, **kwargs):
        super(SociosSuscriptoresForm, self).__init__(*args, **kwargs)

        # for example change class for integerPolje1
        self.fields['nombre'].widget.attrs['class'] = 'input'
        self.fields['apellido'].widget.attrs['class'] = 'input'
        self.fields['mail'].widget.attrs['class'] = 'input'
        self.fields['telefono'].widget.attrs['class'] = 'input'
        self.fields['nacimiento'].widget.attrs['class'] = 'input'
        self.fields['lugar_de_residencia'].widget.attrs['class'] = 'input'
        self.fields['mensaje'].widget.attrs['class'] = 'textarea'
        
        #self.fields['pais'].widget = TextInput(attrs={
         #   'id': 'pais'})
            
        #self.fields['provincia'].widget = TextInput(attrs={
         #   'id': 'provincia'
            
        #})


    

    



class ContactoForm(forms.ModelForm):
    class Meta:
        model= ContactoModel
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)

        # for example change class for integerPolje1
        self.fields['nombre'].widget.attrs['class'] = 'input'
        self.fields['mail'].widget.attrs['class'] = 'input'

        self.fields['mensaje'].widget.attrs['class'] = 'textarea'
        



    
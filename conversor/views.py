from django.shortcuts import render
from .forms import FormularioBinario

def convertir_binario_a_decimal(binario):
    try:
        #Convierte de un numero decimal a binario
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return None

def convertir_decimal_a_octal(decimal):
    try:
        # Convierte de un numero decimal a octal
        octal = oct(decimal)[2:] # Eliminar el prefijo '0o'
        return octal
    except ValueError:
        return None
    
def convertir_decimal_a_hexadecimal(decimal):
    try:
        #Convierte de un numero decimal a hexadecimal
        hexadecimal = hex(decimal)[2:].upper()  # Eliminar el prefijo '0o'
        return hexadecimal;
    except ValueError:
        return None

def conversor(request):
    # Vista para renderizar la página del conversor
    context = {}

    formulario = FormularioBinario();

    if request.method == 'POST':
        formulario = FormularioBinario(request.POST);
        
        if formulario.is_valid():
            try:    
                binario = formulario.cleaned_data['binario'];
                decimal = convertir_binario_a_decimal(binario);
                octal = convertir_decimal_a_octal(decimal);
                hexadecimal = convertir_decimal_a_hexadecimal(decimal);

                context['binario'] = binario;
                context['decimal'] = decimal;
                context['octal'] = octal;
                context['hexadecimal'] = hexadecimal;
            
            except Exception as e:
                formulario.add_error(None, f'Error en la conversión: {str(e)}')
            
            
    context['formulario'] = formulario;
    
    return render(request, 'conversor/conversor.html', context)
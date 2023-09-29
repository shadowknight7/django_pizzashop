from django.shortcuts import render

# Create your views here.
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
def homepage(request):
    return render(request,'pizza/home.html')

def order(request):
    multiple_pizza_form = MultiplePizzaForm()  #empty form
    if request.method=='POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'thanks for ordering %s %s and %s'%(filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'],filled_form.cleaned_data['size'])
            new_form = PizzaForm()
            return render(request,'pizza/order.html',{"pizzaform":new_form,'note':note,'pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})
    else:
        form = PizzaForm()  # constructor
        return render(request, 'pizza/order.html', {"pizzaform": form,'pizza_form':multiple_pizza_form})

def pizzas(request):
    number_of_pizzas = 2
    multiple_filled_form = MultiplePizzaForm(request.GET)
    if multiple_filled_form.is_valid():
        number_of_pizzas = multiple_filled_form.cleaned_data['number']
        print(number_of_pizzas)
        print(multiple_filled_form['number'])
    PizzaFormSet = formset_factory(PizzaForm,extra=number_of_pizzas)
    FormSet = PizzaFormSet()
    if request.method == 'POST' :
            filled_multiple_form = PizzaFormSet(request.POST)
            if filled_multiple_form.is_valid():

                for form in filled_multiple_form:
                    form.save()
                note = 'order placed!!'
            else:
                note = 'order not placed, please try again'
            return render(request,'pizza/pizzas.html', {'formset': filled_multiple_form,'note':note})
    else:

            return render(request,'pizza/pizzas.html',{'formset':FormSet})

def edit(request,pk):
    form_obj = Pizza.objects.get(pk = pk)
    form = PizzaForm(instance=form_obj)
    if request.method=='POST':
        filled_form= PizzaForm(request.POST,instance=form_obj)
        if filled_form.is_valid():
            filled_form.save()
            note = 'your order has been edited sucessfully'
        else:
            note = 'order not edited try again'
        return render(request, 'pizza/edit.html', {'pizzaform': filled_form, 'pizza': form_obj,'note':note})

    else:


        return render(request,'pizza/edit.html',{'pizzaform':form,'pizza':form_obj})




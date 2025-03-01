from django.shortcuts import get_object_or_404, render,redirect
from .models import Expense
from .forms import ExpensesForm 

def expenses_list(request): 
    expenses = Expense.objects.all()
    return render(request, 'listexpenses.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    else:
        form = ExpensesForm()
    return render(request, 'expenses_form.html', {'form': form})

def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)  # ✅ Fix this line

    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    else:
        form = ExpensesForm(instance=expense)
    return render(request, 'expenses_form.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expenses_list')

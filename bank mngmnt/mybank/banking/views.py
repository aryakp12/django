from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Account

def home(request):
    return render(request, 'banking/home.html')

def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return JsonResponse({
        'name': account.name,
        'balance': float(account.balance)
    })

def transfer(request):
    if request.method == 'POST':
        from_account_id = request.POST.get('from_account')
        to_account_id = request.POST.get('to_account')
        amount = float(request.POST.get('amount'))

        from_account = get_object_or_404(Account, id=from_account_id)
        to_account = get_object_or_404(Account, id=to_account_id)

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            return JsonResponse({'status': 'success', 'message': 'Transfer successful!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Insufficient balance!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
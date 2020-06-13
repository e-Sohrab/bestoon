from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from web.models import User, Token, Expense, Income
# Create your views here.

@csrf_exempt
def submit_expense(request):
    """user request and see the submit view"""
    #TODO: token, amount and other parameters might br fake 
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user=this_user, amount=request.POST['amount'], 
        text=request.POST['text'], date=date) #TODO: user might 
    print("i'm in submit expense")
    print(request.POST)

    return JsonResponse({
        'status':'ok',
    }, encoder=json.JSONEncoder)
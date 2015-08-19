from django.shortcuts import render, redirect
from .models import OwingList, Person, Currency, Transaction, Payment
import math

def index(request):
    lists = OwingList.objects.order_by('create_date')
    context = {'lists': lists}
    return render(request, 'owings/main.html', context)

def settle(request, list_id):
    owing_list = OwingList.objects.get(id=int(list_id))
    people = owing_list.person_set.all()
    transactions = owing_list.get_transactions()
    payments = owing_list.get_payments()
    #target_currency = Currency.objects.get(iso_code='SEK' or request.GET.get('currency'))
    target_currency = Currency.objects.get(iso_code='SEK')

    persons = []
    for person in people:
        persons.append({
            'name': person.name,
            'amount': 0.0,
            'id': person.id
        })

    total = 0
    for transaction in transactions:
        exchange_rate = transaction.currency.exchange_rate
        total += transaction.amount / exchange_rate
        for person in persons:
            if person['id'] == transaction.person.id:
                person['amount'] += transaction.amount / exchange_rate

    for payment in payments:
        exchange_rate = payment.currency.exchange_rate
        for person in persons:
            if person['id'] == payment.from_person.id:
                person['amount'] += payment.amount / exchange_rate
        for person in persons:
            if person['id'] == payment.to_person.id:
                person['amount'] -= payment.amount / exchange_rate

    average = total / len(persons)

    settlements = []
    for person in persons:
        if person['amount'] > average:
            needs = person['amount'] - average
            for person_2 in persons:
                if person_2['amount'] < average:
                    can_pay = average - person_2['amount']
                    if needs > can_pay:
                        amount = can_pay
                    else:
                        amount = needs

                    person['amount'] -= amount
                    person_2['amount'] += amount

                    local_amount = amount * target_currency.exchange_rate
                    settlement = {
                        'from': person_2['name'],
                        'from_id': person_2['id'],
                        'to': person['name'],
                        'to_id': person['id'],
                        'amount': '%.2f' % local_amount,
                    }
                    if math.fabs(local_amount) > 0.01:
                        settlements.append(settlement)
                    continue

    context = {
        'list': owing_list,
        'settlements': settlements,
        'currency': target_currency,
    }
    return render(request, 'owings/settle.html', context)

def trip(request, list_id):
    owing_list = OwingList.objects.get(id=int(list_id))
    people = owing_list.person_set.all()
    currencies = Currency.get_active()

    transactions = owing_list.get_transactions()
    payments = owing_list.get_payments()
    
    context = {
        'list': owing_list,
        'people': people,
        'currencies': currencies,
        'expenses': transactions,
        'payments': payments,
    }
    return render(request, 'owings/list.html', context)

def delete_person(request, person_id):
    person = Person.objects.get(id=int(person_id))
    
    for t in person.transaction_set.all():
        t.delete()

    for p in person.payments.all():
        p.delete()

    for p in person.payment_set.all():
        p.delete()

    list_id = person.owing_list_id
    person.delete()
    return redirect('/list/%s' % list_id)

def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=int(transaction_id))
    list_id = transaction.person.owing_list_id
    transaction.delete()
    return redirect('/list/%s' % list_id)

def add_transaction(request, list_id):
    owing_list = OwingList.objects.get(id=int(list_id))
    person = Person.objects.get(id=int(request.POST.get('person_id')))
    currency = Currency.objects.get(id=int(request.POST.get('currency_id')))
    amount = request.POST.get('amount')

    transaction = Transaction()
    transaction.person = person
    transaction.currency = currency
    transaction.amount = amount
    transaction.save()
    return redirect('/list/%s' % list_id)

def add_payment(request):
    first = Person.objects.get(id=int(request.POST.get('from_id')))
    second = Person.objects.get(id=int(request.POST.get('to_id')))
    amount = float(request.POST.get('amount'))
    currency = Currency.objects.get(id=int(request.POST.get('currency_id')))

    payment = Payment()
    payment.from_person = first
    payment.to_person = second
    payment.currency = currency
    payment.amount = amount
    payment.is_settlement = True
    payment.save()

    list_id = first.owing_list.id

    return redirect('/settle/%s' % list_id)

def add_list(request):
    owing_list = OwingList()
    owing_list.name = request.POST.get('list-name')
    owing_list.save()
    return redirect('/list/%s' % owing_list.id)

def add_person_to_list(request, list_id):
    owing_list = OwingList.objects.get(id=int(list_id))
    person = Person()
    person.name = request.POST.get('person-name', 'Snurrar')
    person.owing_list = owing_list
    person.save()
    return redirect('/list/%s' % list_id)

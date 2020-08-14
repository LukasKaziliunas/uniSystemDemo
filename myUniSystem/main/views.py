from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account

def main(request):
    #account = Account.objects.create_user("joemama@gnail.com", "Andrius", "Paulauskas", "yeet123")
    last = Account.objects.last()
    currentUser = request.user
    return render(request, "main.html", {"last": last, "user": currentUser})
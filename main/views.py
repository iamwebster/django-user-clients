from django.shortcuts import render
from users_app.models import Client

from django.contrib.auth.decorators import login_required


@login_required()
def main_page(request):
    clients = Client.objects.filter(responsible=request.user)
    return render(request, 'main/main_page.html', {'clients': clients})
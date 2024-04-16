from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users_app.models import Client


@login_required()
def main_page(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        status = request.POST.get('status')
        client = Client.objects.get(id=client_id)
        if client.status != status:
            client.status = status
            client.save()

        return redirect('main')

    clients = Client.objects.filter(responsible=request.user)
    return render(request, 'main/main_page.html', {'clients': clients})
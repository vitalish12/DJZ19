from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'main/contacts.html')
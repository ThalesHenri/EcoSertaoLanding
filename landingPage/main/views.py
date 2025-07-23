from django.shortcuts import render
from .emailSender import EmailSender
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
   return render(request, 'main/index.html')


@csrf_exempt
def enviarMensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        nomeFantasia = request.POST.get('nomeFantasia')
        email = request.POST.get('email')
        carteiro = EmailSender()
        carteiro.startserver()
        subject = f"Cadastro realizado: {nome} ({email})"
        mensagem = f"Nome: {nome}\nCNPJ: {cnpj}\nTelefone: {telefone}\nNome Fantasia: {nomeFantasia}\nEmail: {email}"
        carteiro.sendMensage(subject, mensagem)        

        
        return render(request, 'main/sucesso.html', {'success': True})

    return render(request, 'main/index.html', {'error': 'Metodo não permitido'})
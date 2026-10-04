from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Funcionario, Servico, Agendamento


# --- ROTAS DE AUTENTICAÇÃO ---


def pagina_login(request):
    if request.user.is_authenticated:
        return redirect("pagina_inicial")
    return render(request, "projetosalaovocacaohair/login.html")


def fazer_login(request):
    if request.method == "POST":
        usuario_input = request.POST.get("username")
        senha_input = request.POST.get("password")

        user = authenticate(request, username=usuario_input, password=senha_input)
        if user is not None:
            login(request, user)
            return redirect("pagina_inicial")
        else:
            return render(
                request,
                "projetosalaovocacaohair/login.html",
                {"error": "Usuário ou senha incorretos."},
            )
    return redirect("pagina_login")


def fazer_logout(request):
    logout(request)
    return redirect("pagina_login")


# --- PÁGINA PRINCIPAL (EXIGE LOGIN) ---


@login_required(login_url="pagina_login")
def pagina_inicial(request):
    funcionarios = Funcionario.objects.all()
    servicos = Servico.objects.all()

    return render(
        request,
        "projetosalaovocacaohair/index.html",
        {"funcionarios": funcionarios, "servicos": servicos, "usuario": request.user},
    )


# --- APIS DO SISTEMA ---


@csrf_exempt
@login_required
def criar_agendamento(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)
            funcionario = Funcionario.objects.get(id=dados.get("funcionario_id"))
            servico = Servico.objects.get(id=dados.get("servico_id"))

            agendamento = Agendamento.objects.create(
                operador=request.user.username,
                cliente=dados.get("cliente"),
                funcionario=funcionario,
                servico=servico,
                data_hora=dados.get("data_hora"),
            )
            return JsonResponse({"sucesso": True, "id": agendamento.id})
        except Exception as e:
            return JsonResponse({"sucesso": False, "erro": str(e)}, status=400)


@csrf_exempt
@login_required
def cadastrar_funcionario(request):
    # Proteção: Apenas administradores podem executar
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "sucesso": False,
                "erro": "Acesso negado: Apenas administradores podem cadastrar funcionários.",
            },
            status=403,
        )

    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get("nome")
        cargo = dados.get("cargo")

        if not nome or not cargo:
            return JsonResponse(
                {"sucesso": False, "erro": "Nome e cargo são obrigatórios."}, status=400
            )

        funcionario = Funcionario.objects.create(nome=nome, cargo=cargo)
        return JsonResponse(
            {
                "sucesso": True,
                "id": funcionario.id,
                "nome": funcionario.nome,
                "cargo": funcionario.cargo,
            }
        )


@csrf_exempt
@login_required
def cadastrar_servico(request):
    # Proteção: Apenas administradores podem executar
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "sucesso": False,
                "erro": "Acesso negado: Apenas administradores podem cadastrar serviços.",
            },
            status=403,
        )

    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get("nome")
        preco = dados.get("preco")

        if not nome or not preco:
            return JsonResponse(
                {"sucesso": False, "erro": "Nome e preço são obrigatórios."}, status=400
            )

        servico = Servico.objects.create(nome=nome, preco=preco)
        return JsonResponse(
            {
                "sucesso": True,
                "id": servico.id,
                "nome": servico.nome,
                "preco": str(servico.preco),
            }
        )


def exportar_dados_json(request):
    agendamentos = list(Agendamento.objects.values())
    return JsonResponse(agendamentos, safe=False)

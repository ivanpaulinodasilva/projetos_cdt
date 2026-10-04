from django.urls import path
from . import views

urlpatterns = [
    # Autenticação
    path('login/', views.pagina_login, name='pagina_login'),
    path('fazer-login/', views.fazer_login, name='fazer_login'),
    path('logout/', views.fazer_logout, name='fazer_logout'),
    
    # Aplicação
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('api/agendar/', views.criar_agendamento, name='criar_agendamento'),
    path('api/exportar-json/', views.exportar_dados_json, name='exportar_json'),
    path('api/cadastrar-funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('api/cadastrar-servico/', views.cadastrar_servico, name='cadastrar_servico'),
]
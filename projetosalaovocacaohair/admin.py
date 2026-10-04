from django.contrib import admin

from django.contrib import admin
from .models import Funcionario, Servico, Produto, Agendamento

admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(Produto)
admin.site.register(Agendamento)

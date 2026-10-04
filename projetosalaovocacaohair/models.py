from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cargo}-{self.nome}"

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    operador = models.CharField(max_length=100)  # Ex: "Recepcionista-Andrei"

    def __str__(self):
        return f"{self.cliente} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

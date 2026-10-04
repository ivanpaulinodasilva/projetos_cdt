// Função para realizar Agendamento
async function realizarAgendamento() {
    const operador = document.getElementById('operador').value;
    const cliente = document.getElementById('cliente').value;
    const funcionario_id = document.getElementById('funcionario').value;
    const servico_id = document.getElementById('servico').value;
    const rawData = document.getElementById('data_hora').value;

    if (!cliente || !funcionario_id || !servico_id || !rawData) {
        alert('Por favor, preencha todos os campos e selecione o funcionário e o serviço!');
        return;
    }

    const data_hora = rawData.replace('T', ' ');

    const payload = {
        operador: operador,
        cliente: cliente,
        funcionario_id: funcionario_id,
        servico_id: servico_id,
        data_hora: data_hora
    };

    try {
        const response = await fetch('/api/agendar/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok && data.sucesso) {
            alert('Agendamento realizado com sucesso! ID: ' + data.id);
            document.getElementById('formAgendamento').reset();
            document.getElementById('funcionario').value = "";
            document.getElementById('servico').value = "";
        } else {
            alert('Erro: ' + (data.erro || 'Falha ao agendar'));
        }
    } catch (err) {
        alert('Erro de conexão com a API.');
    }
}

// Função para cadastrar Funcionário
async function cadastrarFuncionario() {
    const nome = document.getElementById('nome_funcionario').value;
    const cargo = document.getElementById('cargo_funcionario').value;

    if (!nome || !cargo) {
        alert('Preencha o nome e o cargo!');
        return;
    }

    try {
        const response = await fetch('/api/cadastrar-funcionario/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, cargo })
        });

        const data = await response.json();
        if (response.ok && data.sucesso) {
            alert(`Funcionário ${data.nome} cadastrado com sucesso!`);
            location.reload();
        } else {
            alert('Erro: ' + (data.erro || 'Falha ao cadastrar'));
        }
    } catch (err) {
        alert('Erro de conexão ao cadastrar funcionário.');
    }
}

// Função para cadastrar Serviço
async function cadastrarServico() {
    const nome = document.getElementById('nome_servico').value;
    const preco = document.getElementById('preco_servico').value;

    if (!nome || !preco) {
        alert('Preencha o nome e o preço!');
        return;
    }

    try {
        const response = await fetch('/api/cadastrar-servico/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, preco })
        });

        const data = await response.json();
        if (response.ok && data.sucesso) {
            alert(`Serviço ${data.nome} cadastrado por R$ ${data.preco}!`);
            location.reload();
        } else {
            alert('Erro: ' + (data.erro || 'Falha ao cadastrar'));
        }
    } catch (err) {
        alert('Erro de conexão ao cadastrar serviço.');
    }
}
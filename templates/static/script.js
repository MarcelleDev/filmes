document.addEventListener('DOMContentLoaded', () => {
    carregarFilmes();

    // Adicionar filme
    document.getElementById('form-filme').addEventListener('submit', (e) => {
        e.preventDefault();
        const titulo = document.getElementById('titulo').value;
        const genero = document.getElementById('genero').value;
        const ano = document.getElementById('ano').value;
        const assistido = document.getElementById('assistido').checked;

        fetch('/filmes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ titulo, genero, ano, assistido })
        })
        .then(response => {
            if (response.ok) {
                carregarFilmes();
                document.getElementById('form-filme').reset();
            }
        });
    });
});

// Listar filmes
function carregarFilmes() {
    fetch('/filmes')
        .then(response => response.json())
        .then(filmes => {
            const lista = document.getElementById('lista-filmes');
            lista.innerHTML = '';
            filmes.forEach((filme, id) => {
                lista.innerHTML += `
                    <div class="filme-item">
                        <h3>${filme.titulo} (${filme.ano})</h3>
                        <p>Gênero: ${filme.genero}</p>
                        <p>Assistido: ${filme.assistido ? 'Sim' : 'Não'}</p>
                        <button onclick="editarFilme(${id})">Editar</button>
                        <button onclick="removerFilme(${id})">Remover</button>
                    </div>
                `;
            });
        });
}

// Remover filme
function removerFilme(id) {
    fetch(`/filmes/${id}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) carregarFilmes();
        });
}

// Editar filme (implemente você!)
function editarFilme(id) {
    // Desafio: Crie um formulário de edição!
    alert('Desafio: Implemente a edição!');
}
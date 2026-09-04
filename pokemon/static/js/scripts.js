/* ============================
     < CHWM := CHAVIERWEBMÍDIA >
     < JS := PÁGINA SCRIPTS.JS >
     ============================ */

const inputPesquisa = document.getElementById('pesquisa-pokemon');
const msgNaoEncontrado = document.getElementById('msg-nao-encontrado');

function filtrarPokemons() {
    const termo = inputPesquisa.value.trim().toLowerCase();
    const itens = document.querySelectorAll('.pokemon-item');
    let algumVisivel = false;

    itens.forEach(item => {
        const nome = item.getAttribute('data-nome');

        if (nome.startsWith(termo)) {
            item.style.display = '';
            algumVisivel = true;
        } else {
            item.style.display = 'none';
        }
    });

    msgNaoEncontrado.style.display = algumVisivel ? 'none' : 'block';
}

if (inputPesquisa) {
    inputPesquisa.addEventListener('input', filtrarPokemons);
}
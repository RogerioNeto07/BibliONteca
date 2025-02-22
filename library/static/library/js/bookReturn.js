document.addEventListener("DOMContentLoaded", function () {
    let isbnInputs = document.querySelectorAll('input[name="isbn"], input[name="livro"]');
    let nomeLivro = document.getElementById("nome-livro");
    let capaLivro = document.getElementById("capa-livro");

    isbnInputs.forEach(isbnInput => {
        isbnInput.addEventListener("change", function () {
            let isbn = this.value.trim();

            if (isbn) {
                fetch(`/biblioteca/buscar-livro/?isbn=${isbn}`, { method: "GET" })
                    .then(response => response.json())
                    .then(data => {
                        if (data.titulo) {
                            if (nomeLivro) nomeLivro.textContent = data.titulo;
                        } else {
                            if (nomeLivro) nomeLivro.textContent = "Livro não encontrado";
                        }

                        if (data.imagem) {
                            if (capaLivro) {
                                capaLivro.src = data.imagem;
                                capaLivro.style.display = "block";
                            }
                        } else {
                            if (capaLivro) capaLivro.style.display = "none";
                        }
                    })
                    .catch(error => console.error("Erro ao buscar livro:", error));
            }
        });
    });
});

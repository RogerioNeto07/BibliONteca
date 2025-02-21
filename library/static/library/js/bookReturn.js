document.addEventListener("DOMContentLoaded", function () {
    let isbnInput = document.querySelector('input[name="livro"]');
    let nomeLivro = document.getElementById("nome-livro");
    let capaLivro = document.getElementById("capa-livro");

    if (isbnInput) {
        isbnInput.addEventListener("change", function () {
            let isbn = this.value.trim();

            if (isbn) {
                fetch(`/biblioteca/buscar-livro/?isbn=${isbn}`, { method: "GET" })
                    .then(response => response.json())
                    .then(data => {
                        if (data.titulo) {
                            nomeLivro.textContent = data.titulo;
                        } else {
                            nomeLivro.textContent = "Livro não encontrado";
                        }

                        if (data.imagem) {
                            capaLivro.src = data.imagem;
                            capaLivro.style.display = "block";
                        } else {
                            capaLivro.style.display = "none";
                        }
                    })
                    .catch(error => console.error("Erro ao buscar livro:", error));
            }
        });
    }
});

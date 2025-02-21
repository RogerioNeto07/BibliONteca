document.addEventListener("DOMContentLoaded", function () {
    let cpfInput = document.querySelector('input[name="leitor"]');

    if (cpfInput) {
        cpfInput.addEventListener("change", function () {
            let cpf = this.value.trim();

            if (cpf) {
                fetch(`/biblioteca/buscar-usuario/?leitor=${cpf}`, { method: "GET" })
                    .then(response => response.json())
                    .then(data => {
                        console.log("Resposta da API:", data);

                        let nomeUsuario = document.getElementById("nome");
                        if (!nomeUsuario) {
                            console.error("Elemento com ID 'nome' não encontrado no HTML!");
                            return;
                        }

                        if (data.nome) {
                            nomeUsuario.textContent = data.nome;
                        } else {
                            nomeUsuario.textContent = "Usuário não encontrado";
                        }
                    })
                    .catch(error => console.error("Erro ao buscar usuário:", error));
            }
        });
    } else {
        console.error("Campo de CPF não encontrado!");
    }
});

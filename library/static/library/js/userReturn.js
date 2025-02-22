document.addEventListener("DOMContentLoaded", function () {
    function buscarUsuario(campo) {
        let inputElement = document.querySelector(`input[name="${campo}"]`);

        if (inputElement) {
            inputElement.addEventListener("change", function () {
                let valor = this.value.trim();

                if (valor) {
                    fetch(`/biblioteca/buscar-usuario/?usuario=${valor}`, { method: "GET" })
                        .then(response => response.json())
                        .then(data => {
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
            console.error(`Campo de ${campo} não encontrado!`);
        }
    }

    buscarUsuario('usuario');
    buscarUsuario('nome');
});

//Arquivo para criar uma tag que possua os elementos da sidebar de bibliotecária
export class SidebarLibrary extends HTMLElement{
    constructor(){
        super();
        this.innerHTML=`
            <!--Coloquem os icons--!>
            <div class="sidebar-options">
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="{% static "global/imgs/icon-home.png"%}" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                        <a href="" class="sidebar-link main-text white bold">Tela Inicial</a>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="static/global/imgs/icon-home.png" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                        <button href="" id="toggle-book" class="sidebar-button main-text white bold">Livros</button>
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-book" style="display: none;">
                        <div class="sub-menu-item">
                            <i class="fa-duotone fa-solid fa-objects-column"></i>
                            <a href="" class="sub-menu-item secundary-text white">Empréstar</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Devolver</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Renovar</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Adicionar</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Listar</a>
                        </div>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="static/global/imgs/icon-home.png" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                    
                        <button href="" id="toggle-user" class="sidebar-button main-text white bold">Usuários</button>
                    
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-user" style="display: none;">
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Cadastro</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Listagem</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Pendências</a>
                        </div>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="static/global/imgs/icon-home.png" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                        <button href="" id="toggle-loan" class="sidebar-button main-text white bold">Empréstimos</button>
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-loan" style="display: none;">
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Todos</a>
                        </div>
                        <div class="sub-menu-item">
                            <img src="">
                            <a href="" class="sub-menu-item secundary-text white">Pendentes</a>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const content = document.getElementById('dropdown-book');
        const toggle = document.getElementById('toggle-book');

        toggle.addEventListener('click', () => {
         if (content.style.display === 'none'){
            content.style.display = 'block';
         } else {
            content.style.display = 'none';
         }
        });

        const contentUser = document.getElementById('dropdown-user');
        const toggleUser = document.getElementById('toggle-user');

        toggleUser.addEventListener('click', () => {
         if (contentUser.style.display === 'none'){
            contentUser.style.display = 'block';
         } else {
            contentUser.style.display = 'none';
         }
        });

        const contentLoan = document.getElementById('dropdown-loan');
        const toggleLoan = document.getElementById('toggle-loan');

        toggleLoan.addEventListener('click', () => {
         if (contentLoan.style.display === 'none'){
            contentLoan.style.display = 'block';
         } else {
            contentLoan.style.display = 'none';
         }
        });

    }
}

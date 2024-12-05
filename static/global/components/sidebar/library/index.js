//Arquivo para criar uma tag que possua os elementos da sidebar de bibliotecária
export class SidebarLibrary extends HTMLElement{
    constructor(){
        super();
        this.innerHTML=`
            <div class="sidebar-options">
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <span class="material-icons icon">grid_view</span>
                    </div>
                    <div class="sidebar-item-link">
                        <a href="" class="sidebar-link main-text white bold">Tela Inicial</a>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <span class="material-icons icon">menu_book</span>
                    </div>
                    <div class="sidebar-item-link">
                        <button id="toggle-book" class="sidebar-button main-text white bold">Livros</button>
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-book" style="display: none;">
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="/library/loan/book" class="sub-menu-item secundary-text white">Empréstar</a>
                        </div>
                        <div class="sub-menu-item">                     
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="library/return/book" class="sub-menu-item secundary-text white">Devolver</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Renovar</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="/library/register/book" class="sub-menu-item secundary-text white">Adicionar</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Listar</a>
                        </div>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <span class="material-icons icon">person</span>
                    </div>
                    <div class="sidebar-item-link">
                        <button id="toggle-user" class="sidebar-button main-text white bold">Usuários</button>
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-user" style="display: none;">
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="/library/register" class="sub-menu-item secundary-text white">Cadastro</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Listagem</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Pendências</a>
                        </div>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <span class="material-icons icon">menu_book</span>
                    </div>
                    <div class="sidebar-item-link">
                        <button href="" id="toggle-loan" class="sidebar-button main-text white bold">Empréstimos</button>
                    </div>
                    <div class="dropdown-sub-menu" id="dropdown-loan" style="display: none;">
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Todos</a>
                        </div>
                        <div class="sub-menu-item">
                            <span class="material-icons sub-icon">subdirectory_arrow_right</span>
                            <a href="" class="sub-menu-item secundary-text white">Pendentes</a>
                        </div>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <i class="material-icons icon">logout</i>
                    </div>
                    <div class="sidebar-item-link">
                        <a href="" class="sidebar-link main-text white bold">Sair</a>
                    </div>
                </div>
            </div>
        `;

        const toggle = document.getElementById('toggle-book');
        const content = document.getElementById('dropdown-book');

        toggle.addEventListener('click', () => {
         if (content.style.display === 'none'){
            content.style.display = 'block';
            localStorage.setItem('bookState', 'open');
         } else {
            content.style.display = 'none';
            localStorage.setItem('bookState', 'closed');
         } 
        });

        const contentUser = document.getElementById('dropdown-user');
        const toggleUser = document.getElementById('toggle-user');

        toggleUser.addEventListener('click', () => {
         if (contentUser.style.display === 'none'){
            contentUser.style.display = 'block';
            localStorage.setItem('userState', 'open');
        } else {
            contentUser.style.display = 'none';
            localStorage.setItem('userState', 'closed');
         }
        });

        const contentLoan = document.getElementById('dropdown-loan');
        const toggleLoan = document.getElementById('toggle-loan');

        toggleLoan.addEventListener('click', () => {
         if (contentLoan.style.display === 'none'){
            contentLoan.style.display = 'block';
            localStorage.setItem('loanState', 'open');
        } else {
            contentLoan.style.display = 'none';
            localStorage.setItem('loanState', 'closed');
         }
        });

        //Pra manter aberto mesmo ao carregar, fehcar apenas com clique
        window.addEventListener('load', ()=> {
            const bookState = localStorage.getItem('bookState');
            const contentBook = document.getElementById('dropdown-book');
            
            const userState = localStorage.getItem('userState');
            const contentUser = document.getElementById('dropdown-user');

            const loanState = localStorage.getItem('loanState');
            const contentLoan = document.getElementById('dropdown-loan');

            bookState==='open' ? contentBook.style.display = 'block' : contentBook.style.display = 'none';
            userState==='open' ? contentUser.style.display = 'block': contentUser.style.display = 'none';
            loanState==='open' ? contentLoan.style.display = 'block': contentLoan.style.display = 'none';
        });
    }
    
}

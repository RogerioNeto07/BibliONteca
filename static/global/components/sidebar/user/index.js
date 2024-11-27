//Arquivo para criar uma tag que possua os elementos da sidebar de user
export class SidebarUser extends HTMLElement {
    constructor(){
        super();
        this.innerHTML=`
            <div class="sidebar-options">
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="static/global/imgs/icon-home.png" alt="" class="sidebar-icon">
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
                        <a href="" class="sidebar-link main-text white bold">Empréstimos</a>
                    </div>
                </div>
                <div class="sidebar-item">
                    <div class="sidebar-item-icon">
                        <img src="static/global/imgs/icon-home.png" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                        <a href="" class="sidebar-link main-text white bold">Sair</a>
                    </div>
                </div>
            </div>
        `
    }
}



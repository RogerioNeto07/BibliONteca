export class SidebarGuest extends HTMLElement {
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
                        <img src="<i class="fa-solid fa-arrow-right-from-bracket" style="color: #ffffff;"></i>" alt="" class="sidebar-icon">
                    </div>
                    <div class="sidebar-item-link">
                        <a href="" class="sidebar-link main-text white bold">Sair</a>
                    </div>
                </div>
            </div>
        `
    }
}
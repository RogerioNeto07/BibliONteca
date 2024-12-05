export class SidebarGuest extends HTMLElement {
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
            </div>
        `
    }
}
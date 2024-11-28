//Arquivo para criar o header padrão de Bibliotecária e usuário
export class HeaderHome extends HTMLElement{
    constructor(){
        super();
        this.innerHTML=`
            <div class="header-content">
                <div></div>
                <div class="user-content">
                    <img src="{% static "global/imgs/icon-home.png" %}" alt="" class="header-icon-notifications">
                    <div class="user-pic"></div>
                    <p class="username secundary-text">NomeUser</p>
                </div>
            </div>
        `
    }
}
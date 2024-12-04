//Arquivo para criar o header padrão de Bibliotecária e usuário
export class HeaderHome extends HTMLElement{
    constructor(){
        super();
        this.innerHTML=`
            <div class="header-content">
                <div></div>
                <div class="user-content">
                    <i class="fas fa-search"></i>
                    <div class="user-pic"></div>
                    <p class="username secundary-text">NomeUser</p>
                </div>
            </div>
        `
    }
}
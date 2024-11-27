//Biblioteca para fazer apenas uma única exportação para as tags de bibli, user e guest no arquivo base.html
import { SidebarUser } from "./sidebar/user/index.js";

customElements.define('sidebar-user', SidebarUser);

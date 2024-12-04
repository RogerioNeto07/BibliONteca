//Biblioteca para fazer apenas uma única exportação para as tags de bibli, user e guest no arquivo base.html
import { SidebarGuest } from "./sidebar/guest/index.js";
import { SidebarUser } from "./sidebar/user/index.js";
import { SidebarLibrary } from "./sidebar/library/index.js";
import { HeaderHome } from "./header/index.js";

customElements.define('sidebar-user', SidebarUser);
customElements.define('sidebar-guest', SidebarGuest);
customElements.define('sidebar-library', SidebarLibrary);
customElements.define('header-home', HeaderHome);

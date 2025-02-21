
def user_group_context(request):
    user_group = "Visitante"  

    if request.user.is_authenticated:
        if request.user.groups.filter(name="Bibliotecario").exists():
            user_group = "Bibliotecario"
        elif request.user.groups.filter(name="Usuarios").exists():
            user_group = "Usuarios"

    return {"user_group": user_group}

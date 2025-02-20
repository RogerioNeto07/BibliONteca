from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class GroupRequiredMixin(AccessMixin):
    group_required = None  
    
    def dispatch(self, request, *args, **kwargs):
        if self.group_required and not request.user.groups.filter(name=self.group_required).exists():
            return redirect('user:login')  

        return super().dispatch(request, *args, **kwargs)

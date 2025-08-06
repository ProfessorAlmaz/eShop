from django.shortcuts import redirect
class IsAuthenticatedMixin:
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["is_authenticated"] = self.request.user.is_authenticated
        if self.request.user.is_authenticated:
            return data
        else:
            return redirect('login-page')

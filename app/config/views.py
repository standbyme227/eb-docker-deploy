from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

__all__ = (
    'index',
)


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'index.html', context)
    pass

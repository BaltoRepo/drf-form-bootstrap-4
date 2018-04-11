from django.shortcuts import render
from .serializers import SnippetSerializer


def forms(request):
    return render(
        request,
        'drfformbootstrap4/demo/forms.html',
        {'serializer': SnippetSerializer()}
    )

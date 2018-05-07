"""
These resources are for tests and the demo page used in development.
"""
from .serializers import DemoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


class DemoForms(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        serializer = DemoSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = DemoSerializer(data=request.data)
        serializer.is_valid()
        # Normally you'd do something different when the serializer is
        # valid vs. when it's invalid, but here
        # we will just show the valid serializer again.
        return Response({'serializer': serializer})


class DemoVertical(DemoForms):
    template_name = 'drfformbootstrap4/demo/vertical.html'


class DemoHorizontal(DemoForms):
    template_name = 'drfformbootstrap4/demo/horizontal.html'


class DemoInline(DemoForms):
    template_name = 'drfformbootstrap4/demo/inline.html'

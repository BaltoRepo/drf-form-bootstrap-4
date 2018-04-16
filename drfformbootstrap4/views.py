from .serializers import DemoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


class DemoForms(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'drfformbootstrap4/demo/forms.html'

    def get(self, request):
        serializer = DemoSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = DemoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        return redirect('root')

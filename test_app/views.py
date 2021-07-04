from test_app.models import TestModel
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import TestModel
from django.forms.models import model_to_dict


class simple(APIView):

    def post(self, request):
        # salviamo il Json che ci viene passato nei form data
        new_test_content = TestModel.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            phone_number=request.data["phone_number"],
            is_live=request.data["is_live"],
            amount=request.data["amount"],
        )

        return JsonResponse({'data': model_to_dict(new_test_content)})

    def get(self, request):
        content = TestModel.objects.all()
        print('zero', list(content))
        print('uno', list(content.values()))

        return JsonResponse({'data': 'ciao'})

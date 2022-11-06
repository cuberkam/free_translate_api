from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):

        return render(request, "index.html")


def page_not_found_view(request, exception):
    return JsonResponse({"details": "Not Found"}, status=HTTPStatus.NOT_FOUND)

import json
import re
from bs4 import BeautifulSoup
import requests

from django.views.generic import CreateView
from djangoProject.forms import InquiryForm
from djangoProject.models import Inquiry
from django.shortcuts import redirect
from django.http import HttpResponse, Http404


def work(request):
    object = Inquiry.objects.latest('id')
    id = object.id
    return HttpResponse(json.dumps(id), content_type='application/json')

def show(id):
    id = re.search("id=(.*)'>", str(id)).group(1)
    object = Inquiry.objects.get(id = id)
    return HttpResponse(json.dumps(object.result), content_type='application/json')

class WebsiteMainView(CreateView):
    model = Inquiry
    template_name = 'mainPage.html'
    form_class = InquiryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            soup = BeautifulSoup(requests.get(form.page).content, 'html.parser')
            result = {}
            for tag in soup.find_all():
                keys = result.keys()
                for key in keys:
                    if str(key) == str(tag.name):
                        break
                result[tag.name] = {
                    'count': len(soup.find_all(tag.name)),
                    'nested': len(soup.select(tag.name)[0].get_text())
                }
            Inquiry.objects.create(page=form.page, result = str(result))
            return redirect('/')
        else:
            print(form.errors)
            return Http404





from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib import messages
from .forms import NumberForm, MLForm
from django.http import HttpResponseRedirect
import requests
from django.shortcuts import render, redirect
import os
from .MLCode import predict_image
from django.core.files.images import ImageFile
from django.core.files.storage import default_storage
from django.core.files import File
from base64 import b64encode


# API LINKS
NUMBERS_API_LINK = "http://numbersapi.com/"
POKEMON_API_LINK = "https://pokeapi.co/api/v2/pokemon/"

# Create your views here.
class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "Welcome to the site")
        return context


class APIPlaygroundView(FormView):
    template_name = "blog/apiPlayground.html"
    form_class = NumberForm
    success_url = "/apiPlayground"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        form_text = str(form.cleaned_data.get("number"))
        context["numbersAPI"] = self.post_to_api(form_text, NUMBERS_API_LINK)
        context["pokemonAPI"] = self.post_to_api(form_text, POKEMON_API_LINK)
        context["mathAPI"] = self.post_to_api(form_text+"/math", NUMBERS_API_LINK)
        messages.info(self.request, "Data successfully posted to APIs")
        return self.render_to_response(context=context)

    def post_to_api(self, form_input, api_link):
        api_response = requests.get(api_link+form_input)
        if api_link == POKEMON_API_LINK:
            pokemon_json = api_response.json()
            return "The #" + form_input + " pokemon is " + pokemon_json["name"]
        else:
            return api_response.text


class MachineLearningDemoView(FormView):
    template_name = "blog/MLDemo.html"
    form_class = MLForm
    success_url = "/MLDemo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            imgpath, classification, score = self.handle_uploaded_file(request.FILES['image'])
            return render(request, self.template_name, {'form': form,
                                                        'image': imgpath,
                                                        'classification': classification,
                                                        'score': score})
        else:
            return render(request, self.template_name, {'form': form})

    def handle_uploaded_file(self, f):
        """
        Main issue at this point is the inability to fucking choose between two stupid ass piece of shit options
        Option fucking 1:
            Store the stupid dumb fuck arse file in the server somewhere:
                it needs to fucking be in static
                we need to fucking make sure the names are different so add a stupid fucking hex or something
                also this isn't great because there's still a stupid chance that too many users upload files at
                    the same dumb fuck time and overload the server (unlikely though)
            Run machine learning code on the dumb fuck file
            Figure out how to fucking retrieve it from the fucking django server files to show to user
            Delete cunt arse file from stupid dumb fuck folder

        Option fucking 2:
            Don't store the file anywhere, fucking keep it in memory or some shit
            When we upload the file, send it as a raw data stream to the ML code (FUCKING DIFFICULT)
            Then somehow display that in memory image to the user
            Avoids the entire storage issue

        :param f:
        :return:
        """
        print(type(f))
        data = f.read()
        print(data)
        encoded = b64encode(data)
        mime = "image/jpeg"
        mime = mime + ";" if mime else ";"
        imgpath = "data:%sbase64,%s" % (mime, str(encoded)[2:-1])
        print(imgpath)
        classification, score = 1, 1
        return imgpath, classification, score

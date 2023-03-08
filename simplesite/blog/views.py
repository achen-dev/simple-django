from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib import messages
from .forms import NumberForm, MLForm
import requests


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


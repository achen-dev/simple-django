from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from .forms import NumberForm, MLForm, NewUserForm, CommentForm, BlogUpdateForm, BlogCreateForm
import requests
from django.shortcuts import render, redirect
from .MLCode import predict_image, detect_image, buffer_to_torch
from base64 import b64encode
from django.contrib.auth import login
from .models import *
from .utils import slugify

# API LINKS
NUMBERS_API_LINK = "http://numbersapi.com/"
POKEMON_API_LINK = "https://pokeapi.co/api/v2/pokemon/"


# Create your views here.
class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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
        uploaded_image = request.FILES['image']
        print(uploaded_image.name)
        if uploaded_image.name.endswith('.jpg') and uploaded_image.size < 5e6 and form.is_valid():
            imgpath, classification, score = self.handle_uploaded_file(uploaded_image)
            return render(request, self.template_name, {'form': form,
                                                        'image': imgpath,
                                                        'classification': classification,
                                                        'score': score})
        else:
            messages.error(self.request, "File too large or not jpg, must be under 5 Megabytes")
            return render(request, self.template_name, {'form': form})

    def handle_uploaded_file(self, f):
        """
            Don't store the file anywhere, keep it in memory
            When we upload the file, send it as a raw data stream to the ML code (DIFFICULT[BUT WE SOLVED IT LEESSSGOO])
            Then somehow display that in memory image to the user
            Avoids the entire storage issue

        :param f:
        :return:
        """
        data = f.read()
        encoded = b64encode(data)
        img_data = buffer_to_torch(data)
        mime = "image/jpeg"
        mime = mime + ";" if mime else ";"
        imgpath = "data:%sbase64,%s" % (mime, str(detect_image(img_data))[2:-1])  # Implements the detection code
        # imgpath = "data:%sbase64,%s" % (mime, str(encoded)[2:-1])
        classification, score = predict_image(img_data)
        return imgpath, classification, score


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request=request, template_name="blog/home.html", context={"register_form": form})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


class BlogFeedView(ListView):
    template_name = "blog/blogFeed.html"
    queryset = Post.objects.filter(status=1).order_by('-created_on')


class BlogDetailView(TemplateView):
    template_name = "blog/blogDetail.html"
    comment_form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        context['post'] = current_post
        context['form'] = form
        try:
            context['commentList'] = Comment.objects.filter(status=1, post=current_post).order_by('-created_on')
        except:
            context['commentList'] = []
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context['form']
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        if form.is_valid:
            print(form)
            content = request.POST.get('content')
            if content is not None:
                print(content)
                comment_object = Comment(post=current_post, content=content, author=request.user, status=1)
                comment_object.save()
                messages.info(self.request, "Comment successfully posted")
                return redirect('blogDetail', slug=self.kwargs['slug'])
        return super(TemplateView, self).render_to_response(context)


class BlogUpdateView(UpdateView):
    model = Post
    form = BlogCreateForm
    template_name = "blog/blogUpdate.html"
    fields = ['title', 'content', 'status']
    success_url = "/blogFeed"


class BlogCreateView(TemplateView):
    template_name = "blog/blogCreate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = BlogCreateForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            post_object = Post(title=request.POST.get('title'), content=request.POST.get('content'),
                               status=request.POST.get('status'), author=request.user,
                               slug=slugify(request.POST.get('title')))
            post_object.save()
            messages.info(self.request, "Blog successfully created")
            return redirect('blogFeed')
        return super(TemplateView, self).render_to_response(context)


class BlogDeleteView(DeleteView):
    model = Post
    success_url = "/blogFeed"


class GameView(TemplateView):
    """
    Create view for hosting a html5 game
    """
    template_name = "blog/game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

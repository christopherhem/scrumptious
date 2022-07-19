from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# try:
from tags.models import Tag

# except Exception:
# Tag = None


# Create your views here.
class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = "tags/list.html"
    paginate_by = 2


class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")

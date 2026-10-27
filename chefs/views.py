from django.db.models import QuerySet, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from chefs.forms import ChefCreateForm, ChefUpdateForm, ChefDeleteForm
from chefs.models import Chef


# Create your views here.

class ChefsDetailsListView(ListView):
    queryset = (
        Chef.objects.all().order_by('-created_at')
    )

    context_object_name = 'chefs'
    paginate_by = 3
    template_name = 'chefs/chefs-details-list.html'

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            ).distinct()

        return queryset

class ChefCreateView(CreateView):
    model = Chef
    form_class = ChefCreateForm
    template_name = 'chefs/chef-add.html'


    def get_success_url(self):
        return reverse_lazy('chefs:details') #todo need to be set to created chef details

def chef_details_view(request, slug):
    chef = Chef.objects.get(slug=slug)
    chef_recipes = chef.recipe_set.all()


    context = {
        'chef': chef,
        'chef_recipes': chef_recipes,
    }

    return render(request, 'chefs/chef-details.html', context)


class ChefUpdateView(UpdateView):
    model = Chef
    form_class = ChefUpdateForm
    template_name = 'chefs/chef-update.html'

    def get_success_url(self):
        return reverse_lazy('chefs:details-single', kwargs={'slug': self.object.slug})

def chef_delete_view(request, slug):
    chef = get_object_or_404(Chef, slug=slug)

    if request.method == 'POST':
        chef.delete()
        return redirect('chefs:details')

    form = ChefDeleteForm(instance=chef)

    context = {
        'chef': chef,
        'form': form,
    }

    return render(request, 'chefs/chef-delete.html', context)
























































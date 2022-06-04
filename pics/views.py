from django.shortcuts import render, redirect
from django.views.generic import ListView
from puppy_pics.models import PuppyPic
from django.forms import ModelForm


# Create your views here.
class PuppyPicView(ListView):
    template_name = 'puppy_pic_list.html'
    model = PuppyPic

    def get_context_data(self, **kwargs):
        context = super(PuppyPicView, self).get_context_data(**kwargs)
        context['form'] = PhotoForm()

        return context

    def post(self, request, *args, **kwargs):
        context = dict(form=PhotoForm())

        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            context['posted'] = form.instance
            if form.is_valid():
                form.save()
                return redirect('puppy_pics_list')

        return render(request, 'puppy_pic_list.html', context)


class PhotoForm(ModelForm):

    class Meta:
        model = PuppyPic
        fields = '__all__'


def upload(request):
    context = dict(backend_form=PhotoForm())
    context["dataset"] = PuppyPic.objects.all().order_by("-id")
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
        return redirect('puppy_pics_list')

    return render(request, 'upload.html', context)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import Tag
from .forms import TagModelForm

# Create your views here.
def index(request):
    """ Homepage where users can view recent tags and tag other users """

    # Create the Form
    tagModelForm = TagModelForm(request.user.username, auto_id="tag_%s")

    # Get a list of recent tags
    tags = Tag.objects.all().order_by('-timestamp')[:100]

    # Get the most recently tagged user, they're it!
    if (tags.first() is not None):
        itUser = tags.first().toTag

    context = {
        'tags': tags,
        'itUser': itUser,
        'tagModelForm': tagModelForm,
    }

    return render(request, "tag/index.html", context)

@login_required(login_url='/login/')
def newTag(request):
    """ Create a new Tag from a Post request """
    if (request.method == "POST"):
        toUserId = request.POST.get('toTag')
        message = request.POST.get('message')

        # Get the relavent user object
        toUser = User.objects.get(pk=toUserId)

        # Create the tag
        newTag = Tag.objects.create(fromTag=request.user, toTag=toUser, message=message)

        # Do something
        return HttpResponse({'newTag':newTag}, content_type='application/json')
    else:
        return redirect('index')
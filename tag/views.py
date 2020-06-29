from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
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

    # Gather some statistics
    mostTaggedObject = Tag.objects.all().values('toTag').annotate(total=Count('toTag')).order_by('-total').first()
    mostTaggedUser = User.objects.get(pk=mostTaggedObject['toTag'])

    context = {
        'tags': tags,
        'itUser': itUser,
        'mostTaggedUser': mostTaggedUser,
        'mostTaggedCount': mostTaggedObject['total'],
        'tagModelForm': tagModelForm,
    }

    return render(request, "tag/index.html", context)

@login_required(login_url='/login/')
def user(request, username):
    # Get the user object
    userObject = User.objects.get(username=username)

    # Get Statistics
    timesTaggedObject = Tag.objects.all().values('toTag').filter(toTag=userObject).annotate(total=Count('toTag')).order_by('-total').first()
    if (timesTaggedObject is not None):
        timesTagged = timesTaggedObject['total'] or 0
    else:
        timesTagged = 0

    mostTaggedUserId = Tag.objects.all().values('fromTag').filter(toTag=userObject).annotate(total=Count('fromTag')).order_by('-total').first()
    if (mostTaggedUserId is not None):
        mostTaggedUser = User.objects.get(pk=mostTaggedUserId['fromTag'])
    else:
        mostTaggedUser = "N/A"

    time_threshold = datetime.now() - timedelta(weeks=1)
    tagsThisWeekObject = Tag.objects.all().values('toTag').filter(toTag=userObject).filter(timestamp__gt=time_threshold).annotate(total=Count('toTag')).order_by('-total').first()
    if (tagsThisWeekObject is not None):
        tagsThisWeek = tagsThisWeekObject['total'] or 0
    else:
        tagsThisWeek = 0

    # Get a list of recent tags
    tags = Tag.objects.all().filter(toTag=userObject).order_by('-timestamp')[:100]

    context = {
        'timesTagged': timesTagged,
        'mostTaggedUser': mostTaggedUser,
        'tagsThisWeek': tagsThisWeek,
        'tags': tags
    }
    return render(request, "tag/user.html", context)

@login_required(login_url='/login/')
def newTag(request):
    """ Create a new Tag from a Post request """
    if (request.method == "POST"):
        # Make sure that the request user is "it", otherwise redirect them back to index
        itUser = Tag.objects.all().order_by("-timestamp").first().toTag

        if (itUser == request.user):
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
    else:
        return redirect('index')
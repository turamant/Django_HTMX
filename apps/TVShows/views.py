from django.shortcuts import render

from apps.TVShows.models import EightiesKidsTVShows


def popup(request):

    if request.htmx:
        id = request.GET.get('id')
        context = {'show': EightiesKidsTVShows.objects.get(id=id)}
        return render(request, 'TVShows/partials/htmx_show_popup.html', context=context)

    context = {'shows': EightiesKidsTVShows.objects.all()}
    return render(request, 'TVShows/base.html', context=context)


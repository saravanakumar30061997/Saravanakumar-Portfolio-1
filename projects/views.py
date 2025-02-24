from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import models

def index(request):
    pro = models.Project.objects.all().order_by('id')
    paginator = Paginator(pro, 3)  # Show 3 items per page
    page_number = request.GET.get('page', 1)  # Get page number from URL query params (default: 1)
    
    # Store the current page in session
    request.session['portfolio_page'] = page_number  

    page_obj = paginator.get_page(page_number)  # Get the paginated page
    return render(request, 'projects/index.html', {'page_obj': page_obj, "context": pro})


def detail(request, proid):
    projects = get_object_or_404(models.Project, pk=proid)

    # Retrieve the stored page number from session (default to 1 if not set)
    portfolio_page = request.session.get('portfolio_page', 1)

    return render(request, 'projects/detail.html', {"context": projects, "portfolio_page": portfolio_page})

from django.shortcuts import render
from .models import UserRegistration
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    username = request.session.get('username')

    # Fetch email datas
    user_data = UserRegistration.objects.all()

    # Get the number of items per page from GET parameters, default to 10
    per_page = request.GET.get('per_page', 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    # Set up pagination
    paginator = Paginator(user_data, per_page)  # Show 10 emails per page
    page_number = request.GET.get('page')
    user_data = paginator.get_page(page_number)

    return render(request, 'table.html', {'user_data': user_data, 'per_page': per_page})

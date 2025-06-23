# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='registration', view=views.registration, name='registration'),

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),
    
    # path for get dealerships
    path(route='get_dealerships', view=views.get_dealerships, name='get_dealerships'),
    
    # path for get dealer details
    path(route='get_dealer_details/<int:dealer_id>', view=views.get_dealer_details, name='get_dealer_details'),
    
    # path for dealer reviews view
    path(route='get_dealer_reviews/<int:dealer_id>', view=views.get_dealer_reviews, name='get_dealer_reviews'),
    
    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

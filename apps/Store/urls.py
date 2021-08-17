from django.urls import path

from . import views

app_name = 'Store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    # name will be used to call with jinja format in html like in base.html as <li><a class="dropdown-item" href="{% url "Store:all_products" %}">All</a></li>
    path('<slug:slug>', views.product_detail, name = 'product_details'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]

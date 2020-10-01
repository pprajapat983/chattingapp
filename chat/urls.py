from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',views.accounts,name="account"),
    path('realaccounts/',views.realaccounts,name="realaccount"),
]

from django.urls import path
from .views import ProfileView, RegisterView, ProfileLoginView, ProfileLogoutView, BalanceReplenishment

app_name = 'app-users'

urlpatterns = [
    path('', ProfileLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', ProfileLogoutView.as_view(),name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('balance-replenishment/', BalanceReplenishment.as_view(), name='balance-replenishment')

]
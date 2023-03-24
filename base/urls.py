from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, SignupView
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenVerifyView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns   = [ 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/',SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('',TaskList.as_view(), name='tasks'), 
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name="vonly"),  # TemplateView

    path('create/', views.TodoCV.as_view(), name="create"),  # CreateView
    path('list/', views.TodoLV.as_view(), name="list"),  # ListView
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name="delete"),  # DeleteView

    path('mixin/', views.TodoMOMCV.as_view(), name="mixin"),  # MultipleObjectMixin, CreateView
    path('<int:pk>/delete2/', views.TodoDelV2.as_view(), name="delete2"),  # DeleteView
]

from django.urls import path
from neighborhood_app import views

app_name = 'neighborhood_app'

urlpatterns = [
    path('about/', views.about.as_view(), name='about'),
    path('team/', views.team.as_view(), name='team'),
    path('credits/', views.credit.as_view(), name='credits'),
    path('jobs/', views.jobs.as_view(), name='jobs'),
    path('faq/', views.faq.as_view(), name='faq')
]

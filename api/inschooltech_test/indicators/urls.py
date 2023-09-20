from django.urls import path

from indicators.views import ResultsView

urlpatterns = [
    path('results/', ResultsView.as_view(),
         name='results')
]

from django.urls import path
from .views import (
    UnifiedKPIView,
    DashboardSummaryView
)

app_name = 'reports'

urlpatterns = [
    # API unifiée pour les KPIs qui s'adapte selon le rôle
    path('dashboard/kpi/', UnifiedKPIView.as_view(), name='unified-kpi'),
    
    # Résumé global du dashboard
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
] 
from django.contrib import admin
from django.urls import path, include
from orcamento.views import ReceitasViewSet, \
    DespesasViewSet, ListaUmaReceita, ListaReceitasMes, ListaDespesasMes, BuscaReceitas, BuscaDespesas, ResumoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:pk>', ListaUmaReceita.as_view()),
    path('receitas/<int:ano>/<int:mes>/', ListaReceitasMes.as_view()),
    path('despesas/<int:ano>/<int:mes>/', ListaDespesasMes.as_view()),
    path('receitas?descricao=<slug:pk>', BuscaReceitas.as_view()),
    path('despesas?descricao=<slug:pk>', BuscaDespesas.as_view()),
    path('resumo/<int:ano>/<int:mes>/', ResumoView.as_view())
]

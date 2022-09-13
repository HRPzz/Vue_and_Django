from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'  # 사이트 첫 화면 - 특정 앱에 속하지 않음

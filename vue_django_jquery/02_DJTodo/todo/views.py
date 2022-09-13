from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from todo.models import Todo


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'


class TodoCV(CreateView):
    model = Todo  # form 을 보여주려면 model 필요
    fields = '__all__'  # 모든 필드 사용
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')  # redirect


class TodoLV(ListView):
    model = Todo  # 테이블에서 가져와야 함
    template_name = 'todo/todo_list.html'


class TodoDelV(DeleteView):
    model = Todo  # 특정 레코드 삭제해야 하므로 테이블 필요
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')  # redirect
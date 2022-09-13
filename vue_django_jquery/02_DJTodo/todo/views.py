from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin

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


# todo_list.html 의 removeBtn 에 연결된 DeleteView
class TodoDelV(DeleteView):
    model = Todo  # 특정 레코드 삭제해야 하므로 테이블 필요
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')  # redirect


class TodoMOMCV(MultipleObjectMixin, CreateView):
    # 다중 상속 에러 방지 팁 => (mixin, main)
    # - ListView 기능은 mixin 으로 처리 => MultipleObjectMixin (object_list 를 template 으로 넘김)
    # - 상속 구조가 좀 더 복잡한 CreateView 를 메인으로 둠

    model = Todo  # form 을 보여주려면 model 필요
    fields = '__all__'  # 모든 필드 사용
    template_name = 'todo/todo_form_list.html'
    success_url = reverse_lazy('todo:mixin')  # redirect

    # CreateView 의 get 메서드 오버라이딩
    def get(self, request, *args, **kwargs):
        # DB 에서 꺼내오는 todo 레코드 리스트
        # 다중 상속 순서로 인해 MultipleObjectMixin 의 get_queryset() 을 먼저 찾음 -> 이후 CreateView 의 get_queryset() 을 찾음
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    # CreateView 의 post 메서드 오버라이딩  
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)


# todo_form_list.html 의 removeBtn 에 연결된 DeleteView
class TodoDelV2(DeleteView):
    model = Todo  # 특정 레코드 삭제해야 하므로 테이블 필요
    success_url = reverse_lazy('todo:mixin')  # redirect

    # DeleteView 의 get 메서드 오버라이딩
    # - get 요청 오자마자 delete 실행 => 페이지 이동 없음 but 페이지 로딩 발생

    # c.f. vue 는 페이지 이동 없음 and 페이지 로딩 없음 (개발자 도구 - Network 확인)

    # c.f. 원래 get, post 로직
    # - get -> form 보여줌 -> template_name 필요 => 페이지 이동 발생
    # - post -> delete 호출
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
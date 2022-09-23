from django.http import JsonResponse
from django.views.generic import ListView

from todo.models import Todo

class ApiTodoLV(ListView):
    model = Todo
    
    def render_to_response(self, context, **response_kwargs):
        # 쿼리셋의 요소(테이블에 저장된 레코드)를 딕셔너리화하고 리스트로 형변환 => [{k: v}, {k: v}]
        todoList = list(context['object_list'].values())

        # 데이터가 딕셔너리가 아니므로 safe=False
        return JsonResponse(data=todoList, safe=False)
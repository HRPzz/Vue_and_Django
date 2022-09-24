from django.http import JsonResponse
from django.views.generic.list import BaseListView

from django.views.generic.edit import BaseDeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo

# 템플릿 처리(Mixin)가 필요 없으므로 Base 뷰를 상속받는 것이 좀 더 효율적
class ApiTodoLV(BaseListView):
    model = Todo
    
    # HttpResponse 말고 JsonResponse 리턴하도록 delete 메서드 오버라이딩
    def render_to_response(self, context, **response_kwargs):
        # 쿼리셋의 요소(테이블에 저장된 레코드)를 딕셔너리화하고 리스트로 형변환 => [{k: v}, {k: v}]
        todoList = list(context['object_list'].values())

        # 데이터 타입 != 딕셔너리 => safe=False 설정 필수
        return JsonResponse(data=todoList, safe=False)


# csrf 유효성 검사 비활성화
@method_decorator(csrf_exempt, name='dispatch')
# 템플릿 처리(Mixin)가 필요 없으므로 Base 뷰를 상속받는 것이 좀 더 효율적
class ApiTodoDelV(BaseDeleteView):
    model = Todo

    # HttpResponse 말고 JsonResponse 리턴하도록 delete 메서드 오버라이딩
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)
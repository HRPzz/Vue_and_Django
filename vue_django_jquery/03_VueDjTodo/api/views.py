from django.http import JsonResponse
from django.views.generic.list import BaseListView

from django.views.generic.edit import BaseDeleteView, BaseCreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict

from todo.models import Todo

# 템플릿 처리(Mixin)가 필요 없으므로 Base 뷰를 상속받는 것이 좀 더 효율적
class ApiTodoLV(BaseListView):
    model = Todo
    
    # HttpResponse 말고 JsonResponse 리턴하도록 메서드 오버라이딩
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

    # HttpResponse 말고 JsonResponse 리턴하도록 메서드 오버라이딩
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)


# csrf 유효성 검사 비활성화
@method_decorator(csrf_exempt, name='dispatch')
# 템플릿 처리(Mixin)가 필요 없으므로 Base 뷰를 상속받는 것이 좀 더 효율적
class ApiTodoCV(BaseCreateView):
    model = Todo
    fields = '__all__'

    # POST 요청 시 'data' 를 key 로 설정하고 POST 로 받은 데이터를 value 로 저장하는 딕셔너리 kwargs 로 장고 내부에서 form 생성
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        # axios.post 로 받은 데이터는 non-form data 이므로 json 형식의 byte string 인 HttpRequest.body 를 딕셔너리로 변환해서 저장해야 함
        kwargs['data'] = json.loads(self.request.body)
        return kwargs

    # HttpResponse 말고 JsonResponse 리턴하도록 메서드 오버라이딩
    def form_valid(self, form):
        print("form_valid()", form)
        self.object = form.save()
        newTodo = model_to_dict(self.object)

        # 테이블(model)에 추가한 레코드(object)를 응답 데이터(dict)로 보내줌
        return JsonResponse(data=newTodo, status=201)

    
    # HttpResponse 말고 JsonResponse 리턴하도록 메서드 오버라이딩
    def form_invalid(self, form):
        print("form_invalid()", form)
        print("form_invalid()", self.request.POST)

        # non-form data 일 경우 HttpRequest.body 사용
        # c.f. axios.post 로 받은 데이터는 form 태그로 받은 데이터가 아니므로 non-form data

        # raw HttpRequest.body 는 byte string 이므로 decode('utf8') 필요
        print("form_invalid()", self.request.body.decode('utf8'))

        # 폼 에러 내용 응답
        return JsonResponse(data=form.errors, status=400)
# Vue.js - Django 연동 웹 프로그래밍

[![Thumbnail_img][Thumbnail_img]][Thumbnail]

[Thumbnail_img]: https://cdn.inflearn.com/wp-content/uploads/ksh_vuejs.jpg
[Thumbnail]: https://github.com/HRPzz/Vue_and_Django/tree/main/01_Vue2cdn_Bootstrap4cdn_Django2

### 최신 버전 소스 코드 제공 (Vue 3.x, Django 4.x)

[04_Vue3Dj4Todo][04_Vue3Dj4Todo]

[04_Vue3Dj4Todo]: https://github.com/HRPzz/Vue_and_Django/tree/main/01_Vue2cdn_Bootstrap4cdn_Django2/04_Vue3Dj4Todo

### 사용한 기술 스택

- `VueCDN`, `AxiosCDN`
- BootstrapCDN => CSS, `jQuery`
- `Django`

### 강사 개발 환경

- OS
  - Windows 10
- IDE / Editor
  - PyCharm 2018.3.2 Community
    - Django 코딩용
    - 단축키 확인: Help - Keymap Reference
  - VS Code
    - Vue 코딩용
    - 파이참 단축키 사용하기: 확장 - IntelliJ IDEA Keybindings 설치
- Module / Library
  - Python 3.7
  - `Django 2.1.5`
  - CDN
    - Bootstrap 4.3.1
      - bootstrap.min.css 4.3.1
      - `jquery.slim.min.js 3.3.1`
      - popper.min.js 1.14.7
      - bootstrap.min.js 4.3.1
    - FontAwesome 5.7.2
    - `Vue 2.x`
    - `axios.min.js 0.18.1`

### 나의 개발 환경

- OS
  - Docker python:3.7 Container (Debian GNU/Linux 11)
- IDE / Editor
  - VS Code
    - 도커 컨테이너에서 코딩하기 위함
- Module / Library
  - Python 3.7
  - `Django 2.1.5`
  - CDN
    - Bootstrap 4.6.2
      - bootstrap.min.css 4.6.2
      - `jquery.slim.min.js 3.5.1`
      - popper.min.js 1.16.1
      - bootstrap.min.js 4.6.2
    - FontAwesome 6.2.0
    - `Vue 2.7.10`
    - `axios.min.js 0.27.2`

### DjTodo URL 설계

| URL 패턴          | 뷰 이름                                    | 템플릿 파일명            |
| ----------------- | ------------------------------------------ | ------------------------ |
| /admin/           | (장고 기본 제공)                           |                          |
| /todo/vonly/      | TodoVueOnlyTV(TemplateView)                | todo_vue_only.html       |
|                   |                                            |                          |
| /todo/create/     | TodoCV(CreateView)                         | todo_form.html           |
| /todo/list/       | TodoLV(ListView)                           | todo_list.html           |
| /todo/99/delete/  | TodoDelV(DeleteView)                       | todo_confirm_delete.html |
|                   |                                            |                          |
| /                 | HomeView(TemplateView)                     | home.html                |
|                   |                                            |                          |
| /todo/mixin/      | TodoMOMCV(MultipleObjectMixin, CreateView) | todo_form_list.html      |
| /todo/99/delete2/ | TodoMixinDelV(DeleteView)                  | 없음(팝업창)             |

### VueDjTodo URL 설계

| URL 패턴             | 뷰 이름                     | 템플릿 파일명                      |
| -------------------- | --------------------------- | ---------------------------------- |
| /admin/              | (장고 기본 제공)            |                                    |
| /                    | HomeView(TemplateView)      | home.html                          |
|                      |                             |                                    |
| /todo/               | TodoTV(templateView)        | todo_index.html (Vue.js 코드 포함) |
|                      |                             |                                    |
| /api/todo/list/      | ApiTodoLV(BaseListView)     | (불필요)                           |
| /api/todo/create/    | ApiTodoCV(BaseCreateView)   | (불필요)                           |
| /api/todo/99/delete/ | ApiTodoDelV(BaseDeleteView) | (불필요)                           |

### django CBV 정리된 사이트: [ccbv][ccbv]

- 클래스형 뷰의 상속 계층을 시각적으로 확인 가능 (hierarchy diagram)
- 메서드 정리 잘 되어 있음

[ccbv]: https://ccbv.co.uk/

### vue 와 django 비교

- todo-html
  - html 파일에 Vue.js 코드를 작성하는 방식
  - 프로그램 종료시, todo 데이터가 사라지는 단점 => 불완전한 웹 프로그램
  - 브라우저 Storage 를 사용하면 todo 데이터가 유지되지만 내 노트북에서만 보이고 다른 토느북에서는 볼 수 없음
- todo-vue-only  (VueOnly 메뉴)
  - 장고에서 todo-html 방식의 html 파일을 그대로 수용하는 방식
  - 테이블 사용 안 함 => todo 데이터 관련 단점은 동일함 => 불완전한 웹 프로그램
  - 뷰 렌더링 => 페이지 이동 없음 (SPA) -> 페이지 로딩 없음
    - Client Rendering
- todo-django-only (DjangoOnly 메뉴)
  - Vue.js 코드 없이 장고 코드만으로 todo 앱 개발하는 방식
  - 테이블 사용 => 다른 사람과 데이터 공유 가능 => 완전한 웹 프로그램
  - 장고 렌더링 => 페이지 이동 자주 발생 (html 3개)
    - Server Rendering
  - 간단하고 쉬운 클래스형 뷰(CBV) 사용
- todo-django-mixin (DjangoMixin 메뉴)
  - 장고 클래스형 뷰의 믹스인 기능을 활용하는 방식
  - 장고 렌더링 => 페이지 이동을 축소함 -> 페이지 로딩 발생
    - Server Rendering
- todo-vue-django (Todo 메뉴)
  - Vue.js - Django 연동 방식 (JSON 포맷)
  - VueOnly 소스(html)에 데이터 처리를 위한 JSON 연동 기능 추가
  - VueOnly html + axios (Vue) + JsonResponse (Django)

- blog-vue-django

### Client Rendering vs Server Rendering

- Rendering
  - DOM + CSSOM = Rendering Tree
    - HTML tag 및 data -> DOM
    - CSS -> CSSOM
  - Layout
  - Painting
  - 렌더링은 항상 브라우저(클라이언트)에서 처리되는 과정

| Client Rendering                                   | Sever Rendering                                    |
| -------------------------------------------------- | -------------------------------------------------- |
| 클라이언트(Vue.js 코드)에서 렌더링                 | 서버(Django 코드)에서 렌더링                       |
| Vue.js 코드에서 DOM/CSSOM 에 필요한 HTML, CSS 생성 | Django 코드에서 DOM/CSSPM 에 필요한 HTML, CSS 생성 |

### Client Rendering

- HTML/CSS 생성되는 곳
  - 첫 화면은 Server Rendering (Django 에서 HTML/CSS 생성)
  - 그 이후에 Client Rendering (Vue.js 에서 HTML/CSS 생성)
- 첫 화면 구성
  - 빈 화면
    - SPA (Single Page Application) 방식
    - Vue.js 의 일반적인 개발 방식
      - Vue CLI (webpack)
      - Vue directive, axios
      - Vue Router, Vuex
    - SEO (Search Engine Optimization) 문제
      - 검색 엔진에 노출되지 않아서 페이지가 홍보가 안 되는 문제
  - 내용 있는 화면
    - Nuxt.js F/W
      - SSR(Server Side Rendering) 방식
      - SEO 문제 해결 가능
      - Client + Server Rendering 방식 => Vue.js 애플리케이션 개발 가능
      - Client/Server 코드 모두 Vue.js
    - 우리 예제 - VueOnly 메뉴
      - 첫 화면 Django Rendering
      - 이후 Vue.js Rendering
      - SEO 문제 해결 가능
        - => Nuxt.js 방식과 유사함

### 장고 개발자의 선택

- 강사의 선택
  - Client 는 Client 전문, Server 는 Server 전문 프레임워크
  - Vue.js 는 React/Angular 등 다른 프레임워크 대비 쉬움
  - Vue.js 는 기존 코드에 적용이 쉽고 점진적으로 적용 가능

|      | Client  | Server  |                  |
| ---- | ------- | ------- | ---------------- |
| 1    | Django  | Django  | DjangoMixin 메뉴 |
| 2    | Vue.js  | Django  | VueOnly 메뉴     |
| 3    | Nuxt.js | Nuxt.js | 모두 Vue.js 코드 |

### Vue vs React

- Vue
  - HTML, JS 분리되어 있음
  - 기존 HTML (e.g. 부트스트랩) 사용하는 경우 유리함
- React
  - 대부분의 코드가 JS 로 구성됨 => JavaScript 가 메인 언어라면 유리함
  - JSX (Javascript XML) 문법으로 HTML 요소 생성 => Component 로 쪼갬
  - babel 라이브러리에 의해 JS 코드로 변환되는 시간 소요됨 => HTML 안에서 CDN 방식으로 React 코딩하지 않음
  - 주로 CRA (Create-React-App) 방식으로 프로젝트 구성

### PyCharm Shortcut Keys

| Keys                    | Description                   |      | Keys     | Description                           |
| ----------------------- | ----------------------------- | ---- | -------- | ------------------------------------- |
| Esc                     | 현재 기능 해제                |      | Ctrl + / | Comment toggle                        |
| Alt                     | Multi Cursor                  |      | Ctrl + x | Cut                                   |
| Ctrl                    | Multi Cursor<br>(VS Code)     |      | Ctrl + c | Copy                                  |
|                         |                               |      | Ctrl + v | Paste                                 |
| Ctrl + Space            | Code Completion               |      | Ctrl + s | Save all                              |
| Ctrl + Space<br>+ Space | Code Completion<br>and Import |      |          |                                       |
|                         |                               |      | Ctrl + y | Delete Line                           |
| Ctrl + Alt + s          | 설정 (Settings)               |      | Ctrl + d | Duplicate Line                        |
|                         |                               |      |          |                                       |
| Ctrl + Alt + Left       | Navigate Back                 |      | Ctrl + f | 찾기                                  |
| Ctrl + Alt + Right      | Navigate Forward              |      | Ctrl + r | 바꾸기                                |
|                         |                               |      | Ctrl + b | 정의한 곳으로 이동<br/>(Ctrl + Click) |

### Todo 앱 설계 (Vue - Django 연동 방식)

#### Vue.js (axios) <- (Json 데이터) -> Django (JsonResponse)

1. Server Rendering

   - 브라우저에서 첫 페이지 요청

   - 첫 페이지는 Django 에서 생성(index.html, css, js, data)해서 클라이언트에게 보냄

2. 이후 화면 렌더링은 Vue.js 코드에서 수행

3. Data 저장은 서버 측의 DB 에 저장 (SQLite)

4. Client-Server 간 Data 연동은 JSON 포맷

5. Client Rendering

   - Vue.js 의 directive/axios 기능 (e.g. 버튼 클릭) 으로 비동기 request
     - Vue.js 의 Virtual DOM 처리 => 화면 깜빡임 없음
     - 데이터만 응답 => 트래픽 감소 => 응답 속도 빠름

   - DRF(Django Rest Framework) 대신 JsonResponse 사용해서 json (data) 만 응답


### Vue - Django 연동 처리 과정 (Json 방식)

#### Vue.js (axios) <- (Json 데이터) -> Django (JsonResponse)

1. Todo 메뉴 클릭 -> (request) -> Django 의 HttpResponse 클래스 -> (response (html/css/Vue.js))
2. 렌더링시 Vue.js 코드 실행 (Vue 인스턴스가 생성되는 시점) -> (axios.get (/api/xxx/)) -> Django 의 JsonResponse 서브클래스 -> (JsonResponse (200, todo 리스트))
3. ADD 버튼 클릭 -> (axios.get (/api/xxx/)) -> Django 의 JsonResponse 서브클래스 -> (JsonResponse (201, 신규 todo))
4. 삭제 버튼 클릭 -> (axios.get (/api/xxx/)) -> Django 의 JsonResponse 서브클래스 -> (JsonResponse (204))

---

## todo-html

- Todo App (뷰)
  - html 에서 Vue CDN 불러오기
  - html 에서 script 코딩 - Vue 인스턴스 생성 - el, data, methods
    - el -> html 태그
    - data 작성 -> vue 의 머스태시 문법인 {{ }} 로 출력

---

## todo-html

- Todo App (뷰)
  - Vue 객체 - methods 작성 -> js 이벤트 리스너 역할
    - methods 에서 this 로 data 에 적힌 항목 접근 가능
    - vue 코드와 html 코드 데이터 연결 => 데이터 바인딩
      - 대부분 vue -> html 로 데이터 전달됨, 반대 방향은 막혀 있음
      - v-model 로 바인딩되는 데이터는 양방향 전달 가능

---

## todo-html

- Todo App (뷰)
  - 뷰 개발 단점
    - 다른 사람이 뷰 데이터를 볼 수 없음
    - 뷰가 종료되면 뷰에 저장된 데이터가 사라짐
    - 브라우저 스토리지에 데이터를 저장해도 다른 사람이 볼 수 없음
  - 결론
    - 데이터 공유하려면 웹 서버, 데이터베이스 필요 => Django

---

## todo-vue-only

- PyCharm 2018.3.2
  - New Project
    - 루트/베이스 폴더 DjTodo
    - python 3.7 가상 환경 v3DjangoVue
      - Make available to all projects 체크
  - 가상환경 패키지 설치
    - File - Settings - Project Interpreter
    - +버튼 - django 검색 (버전 2.1.5) - Install Package 클릭
  - 터미널
    - django-admin --version # 장고 버전 확인
    - django-admin startproject mysite . # 장고 프로젝트 mysite 생성
    - django-admin startapp todo # 앱 todo 생성
    - python manage.py migrate # db, table 생성
    - python manage.py createsuperuser # 관리자 계정 생성

---

## todo-vue-only

- 장고 개발 패턴
  - MTV
- 장고 개발 순서
  - settings.py
    - INSTALLED_APP 에서 todo 등록
    - TEMPLATES 의 DIRS 등록
    - TIME_ZONE 는 Asia/Seoul 로 변경, USE_TZ 는 False 로 변경
    - STATICFILES_DIRS 등록
  - models.py
    - 테이블 추가 안 하므로 넘어감
  - urls.py
    - mysite/urls.py 에서 todo.urls 를 include
    - todo/urls.py 에서 app_name 은 todo, path 는 'vonly', TodoVueOnlyTV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - TodoVueOnlyTV 클래스
        - TemplateView 상속
        - template_name 으로 html 연결
  - templates
    - todo/templates/todo/todo_vue_only.html
      - HtmlTodo 의 booktodo.html 코드 그대로 가져옴
- 파이참에서 장고 서버 실행 환경 구성
  - Add Configuration - +버튼 - Python - 실행 환경 이름 DjTodoRun 작성, 스크립트 path 는 manage.py 설정, 파라미터는 runserver 작성 - OK
  - 이후 실행 아이콘 클릭하면 장고 실행됨
- 웹 페이지 동작 확인
  - vue 의 머스태시 문법 {{ }} 이 django 의 템플릿 문법 {{ }} 과 겹치는 문제 해결하기
    - vue 의 머스태시 문법 {{ }} 을 { } 로 동작할 수 있게 설정 (Vue 객체의 delimiters 설정)
    - html 코드에서 {{ }} 을 { } 로 변경
  - 로직
    - 서버 django 는 그저 html 을 그대로 보여주는 것만 하는 중
    - 클라이언트 vue 에서 todo 앱의 추가/삭제 담당

---

## todo-django-only

- todo 앱 UI
  - form 보여주고 사용자 입력 받는 부분 (CreateView)
  - DB 내용을 리스트로 보여주는 부분 (ListView)
  - todo 항목 하나를 삭제하는 부분 (DeleteView)

- 장고 CBV
  - CreateView: 폼에 입력한 내용으로 DB 에 레코드를 생성하는 뷰
  - ListView: DB 에서 레코드 목록을 가져와 보여주는 뷰
  - UpdateView: DB 에 있는 특정 레코드를 수정하는 뷰
  - DeleteView: DB 에 있는 특정 레코드를 삭제하는 뷰

---

## todo-django-only

- 앞서 만든 장고 프로젝트 그대로 사용할 예정
- 장고 개발 순서
  - settings.py
    - 수정 사항 없음
  - models.py
    - Todo 클래스(테이블) 작성 - name, todo 컬럼, str 메서드 작성
  - admin.py
    - 데코레이터 @admin.register(Todo) 사용해서 Todo 테이블 등록
    - TodoAdmin 클래스 작성 - list_display 로 보여줄 컬럼 설정
  - 터미널 명령어
    - python manage.py showmigrations # 현재 상태 확인
    - python manage.py makemigrations # 마이그레이션 파일 생성
    - python manage.py migrate # db 반영
  - urls.py
    - mysite/urls.py 는 변경 사항 없음
    - todo/urls.py
      - path 로 'create', TodoCV 뷰 연결
      - path 로 'list', TodoLV 뷰 연결
      - path 로 'delete', TodoDelV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - TodoCV
        - CreateView 상속
        - template_name 으로 html 연결
        - form 이 필요하므로 model, fields 오버라이딩
        - form 처리가 끝난 후 redirect 시켜야 하므로 success_url 설정
          - reverse_lazy 사용
      - TodoLV
        - ListView 상속
        - template_name 으로 html 연결
        - 테이블에서 가져와야 하므로 model 오버라이딩
      - TodoDelV
        - DeleteView 상속
        - template_name 으로 html 연결
        - 특정 테이블에서 특정 레코드를 삭제해야 하므로 model 오버라이딩
        - form 만들 일 없으므로 fields 오버라이딩 필요 없음
        - 삭제 처리 끝난 후 redirect 시켜야 하므로 success_url 설정
          - reverse_lazy 사용
  - templates

---

## todo-django-only

- 장고 개발 순서
  - ...
  - templates
    - todo/templates/todo/todo_form.html
      - todo_vue_only.html 내용 복붙하고 vue 코드 삭제 및 코드 수정
        - form, post, csrf_token
        - v-model 대신 name 설정 => todo 테이블의 컬럼명과 동일해야 함
        - button type submit
    - todo/templates/todo/todo_list.html
      - todo_vue_only.html 내용 복붙하고 vue 코드 삭제 및 코드 수정
        - v-for 대신 django 의 템플릿 문법 {% for %} 으로 변경
        - vue 의 머스태시 문법을 django 의 템플릿 문법으로 변경
        - 삭제 버튼 클릭시 a 태그로 url 연결 => views.py 의 delete 와 연결됨
    - todo/templates/todo/todo_delete.html
      - todo_vue_only.html 내용 복붙하고 vue 코드 삭제 및 코드 수정
        - 기존의 id='app' 인 div 태그 안의 코드 모두 삭제 후 새로 코딩
        - form, post, csrf_token
        - button type submit
- 코드 보완
  - models.py
    - save 메서드 오버라이딩

---

## todo-django-only

- 메인 페이지 만들기
  - mysite/urls.py
    - path 로 '', HomeView 뷰 연결
  - mysite/views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - HomeView
        - TemplateView 상속
        - template_name 으로 html 연결
  - DjTodo/templates/base.html
    - 특정 앱에 속하지 않으므로 루트 디렉토리에서 만듦
    - 최상단에 {% load staticfiles %} 작성 
      - django 3.x 부터는 {% load static %} 작성
    - favicon 설정
      - 구글링해서 나온 사이트 중 favicon.cc 사이트에서 생성
      - DjTodo/static/img/favicon.ico
    - CDN
      - css
        - bootstrap 4.3.1
        - fontawesome 5.7.2
      - js
        - jquery (bootstrap 4.3.1 에 있음)
        - popper (bootstrap 4.3.1 에 있음)
        - bootstrap (bootstrap 4.3.1 에 있음)

---

## todo-django-only

- 모든 html 에서 부트스트랩을 활용한 네비 바 만들기
  - DjTodo/templates/base.html
    - 미리 만들어 놓은 네비 바 코드 붙여넣기
    - head
      - {% block title %} {% endblock %}
      - {% block extra-style %} {% endblock %}
    - body
      - {% block content %} {% endblock %}
      - {% block footer %} {% endblock %}
      - {% block extra-script %} {% endblock %}
  - todo/templates/todo 폴더 안에 있는 모든 html 수정
    - 최상단에 {% extends 'base.html' %} 작성
    - block 설정 - title, extra-style, content, extra-script
    - 모든 버튼을 부트스트랩 버튼으로 변경
    - inputBox 의 line-height 설정
  - DjTodo/templates/home.html
    - 최상단에 {% extends 'base.html' %} 작성
    - 최상단에 {% load staticfiles %} 작성 
      - django 3.x 부터는 {% load static %} 작성
    - 미리 만들어 놓은 코드 붙여넣기
      - DjTodo/static/img/lion.jpg

---

## todo-django-mixin

- 장고 개발 순서
  - settings.py
    - 수정 사항 없음
  - models.py
    -  수정 사항 없음
  - urls.py
    - path 로 'mixin', TodoMOMCV 뷰 연결
  - templates
    - todo/templates/todo/todo_form_list.html
      - form - CreateView
      - todo_list.html 의 ul 복붙 - ListView
        - object_list 라는 context 를 view 에서 template 으로 넘겨줘야 함
    - DjTodo/templates/base.html
      - 아이템 url 은 todo:mixin 인 네비 바 링크 DjangoMixin 추가
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - TodoMOMCV
        - (MultipleObjectMixin, CreateView) 다중 상속
          - 상속 계층이 좀 더 복잡한 CreateView 를 메인으로 두고 ListView 는 Mixin 으로 처리해야 에러 줄일 수 있음
            - CreateView
              - CreateView 는 form 처리 때문에 ListView 보다 상속 계층이 복잡함
              - 기능 단위로 구현된 Mixin 을 상속받아서 만들어진 CreateView
              - [ccbv][ccbv] 사이트에서 view 별로 hierarchy diagram 을 보면 상속 계층 복잡도를 비교해볼 수 있음
            - ListView
              - object_list 라는 context 를 view 에서 template 으로 넘겨주는 기능이 MultipleObjectMixin 클래스에 정의되어 있음
              - self.object_list 준비해야 함
          - 코딩으로는 (mixin, main) 순서로 작성해야 함 => (MultipleObjectMixin, CreateView)
            - 대부분의 기능은 main 이 되는 CreateView 에서 처리
            - main 이 되는 CreateView 에서 없는 기능이 mixin 이 되는 MultipleObjectMixin 에서 처리
        - template_name 으로 html 연결
        - CreateView 에서 form 처리를 하기 위해 model, fields 오버라이딩
        - form 처리가 끝난 후 redirect 시켜야 하므로 success_url 설정
        - get 메서드 오버라이딩 => self.object_list = self.get_queryset()
          - db 에서 todo item 을 꺼내옴
          - 다중 상속한 클래스 모두 get_queryset 메서드를 가지고 있을 경우 앞에 적힌 클래스에 있는 get_queryset 메서드로 실행됨
          - 리턴값으로 상위 get 메서드 호출 => return super().get(request, *args, **kwargs)
        - post 메서드 오버라이딩 => self.object_list = self.get_queryset()
          - get 메서드와 마찬가지

---

## todo-django-mixin

- todo/templates/todo/todo_form_list.html
  - removeBtn 에서 a 태그 url 을 todo:delete2 로 변경
- urls.py
  - path 로 'delete2', TodoDelV2 뷰 연결
- views.py
  - urls.py 에서 작성한 path 에 맞춰서 작성
    - TodoDelV2
      - DeleteView 상속
      - template_name 으로 html 연결
      - 삭제 처리 끝난 후 redirect 시켜야 하므로 success_url 설정
        - reverse_lazy 사용
- 페이지 이동 없이 (but 페이지 로딩 발생) 레코드 삭제하도록 변경하기
  - 기존 로직: mixin html (todo_form_list.html) 에서 removeBtn 버튼 클릭 -> (get 요청) -> deleteView 에서 todo_delete_confirm.html 보여줌 -> confirm 버튼 클릭 -> (post 요청) -> db 에서 해당 레코드 삭제, mixin 으로 redirect
  - 변경할 로직: get 요청 처리 생략하고 post 요청만 처리하면 됨
    - deleteView 의 get 메서드 오버라이딩
      - get 메서드에서 폼을 보여주지 않고 곧바로 post 처리하면 됨
      - 폼을 보여주지 않으므로 template_name 필요 없음

- 정말 삭제하시겠습니까 팝업창 띄우기 (페이지 이동 없음 but 페이지 로딩 발생)
  - todo_form_list.html
    - 팝업창
      - 부트스트랩 - 컴포넌트 - 모달
      - 미리 작성한 html, js 코드 가져옴
    - removeBtn
      - TodoDelV2 연결 삭제
      - data-toggle, data-target 설정해서 modal 연결
      - 데이터 넘겨주기 위해 data-id, data-name, data-todo 정의

---

## todo-vue-django

- PyCharm 2018.3.2
  - New Project
    - 루트/베이스 폴더 VueDjTodo
    - 기존에 만들어 놓은 python 3.7 가상 환경 v3DjangoVue 그대로 사용
  - 터미널
    - django-admin startproject mysite . # 장고 프로젝트 mysite 생성
    - django-admin startapp todo # 앱 todo 생성
    - python manage.py migrate # db, table 생성
    - python manage.py createsuperuser # 관리자 계정 생성

- 장고 개발 순서
  - settings.py
    - INSTALLED_APP 에서 todo 등록
    - TEMPLATES 의 DIRS 등록
    - TIME_ZONE 는 Asia/Seoul 로 변경, USE_TZ 는 False 로 변경
    - STATICFILES_DIRS 등록
  - models.py
    - 테이블 추가 안 하므로 넘어감
  - mysite/urls.py
    - path 로 '', HomeView 뷰 연결
  - mysite/views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - HomeView
        - TemplateView 상속
        - template_name 으로 html 연결
  - templates
    - VueDjTodo/templates/base.html, VueDjTodo/templates/home.html
      - DjTodo/templates 폴더 복붙하고 코드 수정
  - static
    - DjTodo/static 폴더 복붙

- 파이참에서 장고 서버 실행 환경 구성
  - Add Configuration - +버튼 - Python - 실행 환경 이름 VueDjTodoRun 작성, 스크립트 path 는 manage.py 설정, 파라미터는 runserver 작성 - OK
  - 이후 실행 아이콘 클릭하면 장고 실행됨

---

## todo-vue-django

- todo app
  - models.py
    - DjTodo/todo/models.py 복붙
  - admin.py
    - DjTodo/todo/admin.py 복붙
  - 터미널 명령어 입력
    - python manage.py makemigrations
    - python manage.py migrate
  - urls.py
    - mysite/urls.py 에서 todo.urls 를 include
    - todo/urls.py 에서 app_name 은 todo, path 는 '', TodoTV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - TodoTV
        - TemplateView 상속
        - template_name 으로 html 연결

---

## todo-vue-django

- todo app
  - todo/templates/todo/todo_index.html
    - DjTodo/todo/templates/todo/todo_vue_only.html 복붙하고 코드 수정
    - 필요한 부분
      - include base.html
      - block title
      - block extra-style
      - block content
        - h1
        - form
          - form 태그가 아니라 div 태그로 구현
          - form 기능으로 서버에 요청 보내는 것이 아니라 vue.js 코드 내에서 서버로 요청 보내야 하기 때문
          - v-model 이름과 테이블 컬럼명이 같아야 데이터 바인딩이 올바르게 됨
        - todo_list

---

## todo-vue-django

- todo app
  - todo/templates/todo/todo_index.html
    - block footer
      - 사용하지 않음 => 추가할 코드 없음
    - block extra-script
      - Vue.js CDN
      - Vue 인스턴스 생성
        - new Vue({ delimiters, el, data, methods, created });
          - delimiters: [[ ]]
            - 뷰의 머스태시 문법 {{ }} 은 장고 템플릿 문법 {{ }} 과 겹쳐서 사용 불가
            - 자바스크립트의 { } 문법 존재
            - [[ ]] 로 사용하는 걸로 변경
          - el: #app
          - data: name, todo, todoList
          - methods: add_todo(), remove_todo()
          - created
- 뷰에서 CRUD 가능 but 다른 페이지로 갔다가 돌아오면 데이터가 사라짐

---

## todo-vue-django

- vue - django 연동
  - todo/templates/todo/todo_index.html
    - axios cdn 추가
    - vue 인스턴스
      - created 훅
        - 뷰 인스턴스가 생성되는 시점에 호출되는 메서드
      - axios 기능은 모두 methods 에서 코딩
        - axios.get().then().catch()
          - 콜백 함수 밖의 this 는 vue 객체를 가리키고 콜백 함수 안의 this 는 window 객체를 가리킴
          - 콜백 함수 밖에서 로컬 변수 vm 에 this (vue 객체) 저장하고 콜백 함수 안에서 this (window 객체) 가 아닌 로컬 변수 vm (vue 객체) 사용

---

## todo-vue-django

- api app
  - 터미널 명령어 입력
    - django-admin startapp api
  - settings.py
    - INSTALLED_APP 에서 api 등록
  - models.py
    - 테이블 추가 안 하므로 넘어감
  - urls.py
    - mysite/urls.py 에서 api.urls 를 include
    - api/urls.py 에서 app_name 은 api, path 는 'todo/list/', ApiTodoLV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - ApiTodoLV 클래스 (axios.get 요청에 대한 응답 보냄)
        - ListView 상속 -> 나중에 BaseListView 로 변경할 예정
        - get 에서 오버라이딩할 부분 찾기
          - [ccbv][ccbv] 사이트 접속 -> ListView 페이지에서 get 메서드 확인
          - get 메서드 로직
            - get_queryset 함수를 통해 해당 테이블로부터 모든 레코드를 가져와서 저장한 변수 queryset 리턴
            - get_context_data 함수를 통해 queryset 을 value 로, 'object_list' 를 key 로 설정한 딕셔너리 context 생성
            - render_to_response 함수를 통해 context 를 입력받은 response_class 리턴
              - 리턴한 response_class 가 바로 HttpResponse 이므로 render_to_response 메서드를 오버라이딩해서 JsonResponse 로 변경하면 됨
        - render_to_response 메서드 오버라이딩
          - JsonResponse
            - Django documentation - The view layer - Reference: Request/response objects - JsonResponse objects 에서 확인
              - data 인자: 클라이언트에게 보낼 데이터
              - safe 인자: 데이터 형식이 딕셔너리가 아닐 경우 반드시 False 설정해야 함
- axios.get 동작 확인
  - 크롬 개발자 도구 - Network - 원하는 url 클릭해서 header, 서버에서 보낸 response 데이터 확인 가능
  - admin 페이지에서 todo 테이블의 레코드 추가 -> todo 페이지에서 해당 데이터를 볼 수 있음
  - todo 페이지에서 삭제버튼 누르면 vue.js 코드 메모리에서만 삭제될 뿐 테이블에서는 삭제되지 않음 -> axios.delete 구현 필요

---

## todo-vue-django

- api app
  - urls.py
    - path 는 'todo/\<int:pk\>/delete/', ApiTodoDelV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - ApiTodoDelV 클래스 (axios.delete 요청에 대한 응답 보냄)
        - 템플릿 처리할 일 없음 => BaseDeleteView 상속
        - delete 에서 오버라이딩할 부분 찾기
          - [ccbv][ccbv] 사이트 접속 -> DeleteView 페이지에서 delete 메서드 확인
          - redirect 필요 없음 => 기존의 return HttpResponseRedirect 에서 JsonResponse 로 변경하면 됨
        - CSRF 방어 기능 설정해야 에러 발생 안 함 -> 임시로 비활성화해두고 실행 결과 확인
          - CSRF Attack: 이미 인증된 가입자의 권한으로 악성 스크립트를 실행시키는 공격 방법
      - ApiTodoLV 클래스 (axios.get 요청에 대한 응답 보냄)
        - 템플릿 처리할 일 없음 => BaseListView 상속으로 변경
- todo/templates/todo/todo_index.html
  - vue 인스턴스
    - axios 기능은 모두 methods 에서 코딩
      - axios.delete().then().catch()
        - 콜백 함수 밖의 this 는 vue 객체를 가리키고 콜백 함수 안의 this 는 window 객체를 가리킴
        - 콜백 함수 밖에서 로컬 변수 vm 에 this (vue 객체) 저장하고 콜백 함수 안에서 this (window 객체) 가 아닌 로컬 변수 vm (vue 객체) 사용
- axios.delete 동작 확인
  - 크롬 개발자 도구 - Network - 원하는 url 클릭해서 header, 서버에서 보낸 response 데이터 확인 가능
  - todo 페이지에서 삭제버튼 누르면 테이블에서 해당 레코드 삭제되고 vue.js 코드 메모리에서도 삭제됨
    - admin 페이지에서 todo 테이블의 레코드가 삭제됐는지 확인
  - todo 페이지에서 ADD 버튼 누르면 vue.js 코드 메모리에서만 추가될 뿐 테이블에서는 추가되지 않음 -> axios.post 구현 필요

---

## todo-vue-django

- vue - django 연동
  - todo/templates/todo/todo_index.html
    - vue 인스턴스
      - axios 기능은 모두 methods 에서 코딩
        - axios.post().then().catch()
          - 콜백 함수 밖의 this 는 vue 객체를 가리키고 콜백 함수 안의 this 는 window 객체를 가리킴
          - 콜백 함수 밖에서 로컬 변수 vm 에 this (vue 객체) 저장하고 콜백 함수 안에서 this (window 객체) 가 아닌 로컬 변수 vm (vue 객체) 사용

---

## todo-vue-django

- api app
  - urls.py
    - path 는 'todo/create/', ApiTodoCV 뷰 연결
  - views.py
    - urls.py 에서 작성한 path 에 맞춰서 작성
      - ApiTodoCV 클래스 (axios.post 요청에 대한 응답 보냄)
        - 템플릿 처리할 일 없음 => BaseCreateView 상속
        - post 에서 오버라이딩할 부분 찾기
          - [ccbv][ccbv] 사이트 접속 -> CreateView 페이지에서 post 메서드 확인
          - post 메서드 로직
            - get_form 함수를 통해 get_form_class 로 만든 form_class 안에 get_form_kwargs 함수를 인자로 넣어주고 리턴
            - get_form_kwargs 함수를 통해 kwargs 를 딕셔너리로 만듦,  POST 요청 시 'data' 를 key 로 설정하고 POST 로 받은 데이터를 value 로 저장
              - Django documentation - The view layer - Reference: Request/response objects - HttpRequest 확인
                - form data 일 경우 HttpRequest.POST 사용
                - non-form data 일 경우 HttpRequest.body 사용
                  - axios.post 로 받은 데이터는 form 태그로 받은 데이터가 아니므로 non-form data
                  - raw HttpRequest.body 는 byte string 이므로 decode('utf8') 필요
            - get_form_kwargs 함수를 통해 kwargs 의 'data' 키에 self.request.body 를 값으로 넣으면 됨
              - self.request.body 는 json 형식의 byte string 이므로 dict 로 타입 변환 필요 => json.loads(self.request.body) 사용하면 됨
                - json 라이브러리
                  - string json -> json: json.loads()
                  - json -> string json: json.dumps()
            - form_valid 함수를 통해 테이블에 레코드 저장
              - 테이블(model)에 추가한 레코드(object)를 응답 데이터(dict)로 보내줌
                - model_to_dict 함수를 사용해서 타입 변환 필요
              - redirect 필요 없음 => 기존의 return HttpResponseRedirect 에서 JsonResponse 로 변경하면 됨
        - CSRF 방어 기능 설정해야 에러 발생 안 함 -> 임시로 비활성화해두고 실행 결과 확인
          - CSRF Attack: 이미 인증된 가입자의 권한으로 악성 스크립트를 실행시키는 공격 방법
- axios.post 동작 확인
  - 크롬 개발자 도구 - Network - 원하는 url 클릭해서 header, 서버에서 보낸 response 데이터 확인 가능
  - todo 페이지에서 ADD 버튼 누르면 테이블에서 해당 레코드 추가되고 vue.js 코드 메모리에서도 추가됨
    - admin 페이지에서 todo 테이블의 레코드가 추가됐는지 확인

---

## todo-vue-django

- remove_todo 에서 정말로 삭제하시겠습니까 기능 구현
  - vue (todo/templates/todo/todo_index.html 의 remove_todo) 에서  confirm 코드 추가
- CSRF 활성화
  - CSRF
    - 서버에서 생성한 csrftoken 을 보냄
    - 클라이언트(브라우저)는 쿠키에 csrftoken저장
      - 크롬 개발자 도구 - Application - Storage - Cookies 에서 도메인별로 저장된 쿠키(csrftoken) 확인 가능
      - 크롬 개발자 도구 - Network - 원하는 url(list/) 클릭 후 Response Hedaers 에서 Set-Cookie 로 csrftoken 존재
    - Vue 에서 쿠키를 찾아서 request header 에 쿠키 값을 넣어서 보냄
      - 쿠키 값: 쿠키이름 csrftoken, 쿠키헤더 X-CSRFToken
        - Django 의 settings.py 에서 쿠키이름, 쿠키헤더명 변경 가능
      - 크롬 개발자 도구 - Network - 원하는 url(create/, delete/) 클릭 후 Request Headers 에서 X-CSRFToken 존재
  - vue (todo/templates/todo/todo_index.html 의 add_todo, remove_todo) 에서 전역 scope (axios.defaults) 로 CSRF 토큰 쿠키 값 설정
    - 이렇게 하면 axios 요청할 때마다 자동으로 헤더에 CSRF 토큰 값을 설정해줌
  - django (todo/views.py) 에서 CSRF 토큰 비활성화 제네레이터(csrf_exempt) 삭제, CSRF 토큰 자동 생성 제네레이터(ensure_csrf_cookie) 추가
    - ApiTodoDelV 와 ApiTodoCV 에 설정한 @method_decorator(csrf_exempt, name='dispatch') 데코레이터 삭제
    - ApiTodoLV 에 @method_decorator(csrf_exempt, name='dispatch') 데코레이터 추가
      - csrftoken 이 없으면 생성하고 클라이언트(Vue)로 넘기는 데코레이터
      - 클라이언트에서 axios post/delete 요청을 보낼 때 CSRF 쿠키를 사용할 수 있게 됨

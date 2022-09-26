from django.db import models


class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)

    def __str__(self):
        return self.todo

    # save 메서드 오버라이딩
    def save(self, force_insert=False, force_update=False, using=None,
            update_fileds=None):
        # 이름 기본값 설정
        if not self.name:
            self.name = '홍길동'
        # DB 에 레코드 저장
        super().save()
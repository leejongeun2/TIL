from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.

class Movie(models.Model): # Movie모델 클래스는 models에 있는 model을 상속받아서 만듦 => 설계는 했지만 기능 자체는 상속을 받아 사용하고 싶기 때문
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time = models.IntegerField()
    content = models.TextField()
    image = ProcessedImageField(upload_to='images/', blank=True, 
    processors=[ResizeToFill(1200, 960)],
    format='JPEG',
    options={'quality':80}) # 항상 업로드하는 것은 아니니 blank=true
# 사용자가 입력한 이미지를 어디로 업로드 할 것이냐!
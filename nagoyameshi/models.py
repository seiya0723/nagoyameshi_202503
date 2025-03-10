from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.urls import reverse

# 会員
User = get_user_model()

# カテゴリ
class Category(models.Model):

    name = models.CharField(verbose_name="名前", max_length=15)
    created_at = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name
    
# 店舗
class Restaurant(models.Model):
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="名前", max_length=50)
    image = models.ImageField(verbose_name="画像", upload_to="media_local/restaurant/")
    description = models.CharField(verbose_name="店舗説明", max_length=500)
    start_at = models.TimeField(verbose_name="営業開始時間", default=timezone.now)
    end_at = models.TimeField(verbose_name="営業終了時間", default=timezone.now)
    cost = models.PositiveIntegerField(verbose_name="価格帯")
    post_code = models.CharField(verbose_name="郵便番号", max_length=8)
    address = models.CharField(verbose_name="住所", max_length=100)
    tel = models.CharField(verbose_name="電話番号", max_length=11)
    created_at = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    
    def __str__ (self):
        return self.name
    
# レビュー
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name="店舗", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE)
 #   star = models.IntegerField(verbose_name="星", validators=[MinValueValidator(1),MaxValueValidator(MAX_STAR)],default=1)
    content = models.CharField(verbose_name="内容", max_length=100)
    created_at = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    """
    def star_icon(self):
        dic               = {}
        dic["true_star"]  = self.star * " "
        dic["false_star"] = ( MAX_STAR - self.star) * " "

        return dic
    """
        
    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('top')
    
# お気に入り
class Favorite(models.Model):
    user = models.ForeignKey(User, verbose_name="登録者", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, verbose_name="店舗", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.restaurant.name

# 予約
class Reservation(models.Model):
    user = models.ForeignKey(User, verbose_name="予約者", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, verbose_name="店舗", on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name="予約日時")
    headcount = models.PositiveIntegerField(verbose_name="人数")
    created_at = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.restaurant.name

# 有料会員と無料会員　見分け
class PremiumUser(models.Model):
    user = models.ForeignKey(User, verbose_name="有料会員", on_delete=models.CASCADE)
    premium_code = models.TextField(verbose_name="有料会員コード")
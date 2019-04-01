from django.db import models


# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=25)
    nickname = models.CharField(max_length=15)
    passwd = models.CharField(max_length=32)
    city = models.CharField(max_length=20, default='沈阳')
    sign = models.CharField(max_length=50, default='人在湖飘')
    gender = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='photo', default='/static/res/images/avatar/00.jpg')
    qq = models.IntegerField(default=0)
    weibo = models.CharField(max_length=20, default='wb')
    join_time = models.DateTimeField(auto_now_add=True)
    kiss_num = models.IntegerField(default=100)
    vip_grade = models.IntegerField(default=0)
    is_bigv = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)

    class Meta:
        db_table = 'userinfo'


class QiandaoInfo(models.Model):
    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    total = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'qiandaoinfo'


class MessageInfo(models.Model):
    content = models.CharField(max_length=100)
    send_user = models.ForeignKey('UserInfo', related_name='send_user_id', on_delete=models.CASCADE)
    recv_user = models.ForeignKey('UserInfo', related_name='recv_user_id', on_delete=models.CASCADE)
    topic = models.ForeignKey('jie.TopicInfo', on_delete=models.CASCADE)
    msg_type = models.IntegerField()
    is_read = models.IntegerField()
    create_time = models.DateTimeField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'messageinfo'

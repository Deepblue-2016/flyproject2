from django.db import models


# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=25)
    nickname = models.CharField(max_length=15)
    passwd = models.CharField(max_length=16)
    city = models.CharField(max_length=20)
    sign = models.CharField(max_length=50)
    gender = models.IntegerField()
    photo = models.ImageField(upload_to='photo')
    qq = models.IntegerField()
    weibo = models.CharField(max_length=20)
    join_time = models.DateTimeField()
    kiss_num = models.IntegerField()
    vip_grade = models.IntegerField()
    is_bigv = models.IntegerField()
    is_active = models.IntegerField()

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

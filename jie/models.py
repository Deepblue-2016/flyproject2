from django.db import models


# Create your models here.
class TopicInfo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    is_delete = models.IntegerField(default=0)
    view_times = models.IntegerField(default=0)
    kiss_num = models.IntegerField(default=0)
    is_top = models.IntegerField(default=0)
    is_good = models.IntegerField(default=0)
    is_over = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    # category = models.ManyToManyField('CategoryInfo', through='TopicCategory')
    category = models.ManyToManyField('CategoryInfo')

    class Meta:
        db_table = 'topicinfo'


class CategoryInfo(models.Model):
    typename = models.CharField(max_length=10)

    class Meta:
        db_table = 'categoryinfo'


class TopicCategory(models.Model):
    topic = models.ForeignKey('TopicInfo', on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'topic_category'


class Comment(models.Model):
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    topic = models.ForeignKey('TopicInfo', on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=300)
    zan_num = models.IntegerField()
    is_accept = models.IntegerField()
    comment_time = models.DateTimeField()

    class Meta:
        db_table = 'comment'


class CommentAgree(models.Model):
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment_agree'

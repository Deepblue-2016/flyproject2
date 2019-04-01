from django.db import models


# Create your models here.
class TopicInfo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    is_delete = models.IntegerField()
    view_times = models.IntegerField()
    kiss_num = models.IntegerField()
    is_top = models.IntegerField()
    is_good = models.IntegerField()
    is_over = models.IntegerField()
    comment_num = models.IntegerField()
    create_time = models.DateTimeField()
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    category = models.ManyToManyField('CategoryInfo', through='TopicCategory')

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

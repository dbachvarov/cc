from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
#from datetime import datetime, timedelta # added for expiration default value
import pytz
import datetime

STATUS_CHOICES =(
    ('Live','Live'),
    ('Expired','Expired')
)

POST_TOPICS = [
    ('POLITICS','Politics'),
    ('HEALTH', 'Health'),
    ('SPORT', 'Sport'),
    ('TECH', 'Tech')

]
class Post (models.Model):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='topic_post', on_delete=models.CASCADE)
    topic = MultiSelectField(choices = POST_TOPICS)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    status  =   models.CharField(max_length=10, choices =STATUS_CHOICES, default = 'Live')
    expiration_time = models.DateTimeField(auto_now =False, auto_now_add=False)
    #expiration_time = models.DateTimeField(default =datetime.datetime.today()+datetime.timedelta(days=2))

    # https://stackoverflow.com/questions/2199013/how-can-my-django-model-datefield-add-30-days-to-the-provided-value
    @property
    def is_active(self):
        now=datetime.datetime.today()
        now = pytz.utc.localize(now)
        if self.expiration_time < now :
            self.status ='Expired'
            self.save()
            return False
        self.status = 'Live'
        self.save()
        return True

   
            
    


#   https://www.codegrepper.com/code-examples/python/how+to+fix+can%27t+compare+offset-naive+and+offset-aware+datetimes
    
    def __str__(self):
        return f"{self.title}-{self.status}"

# https://medium.com/djangotube/django-like-and-dislike-buttons-model-design-like-youtube-f152b95e7f21
class Comment(models.Model):            # validate post status
    def validate_status(value):
        data = Post.objects.get(pk=value)
        if str(data.status)=='Expired':
            raise ValidationError('Status of the post is expired')

    post   =  models.OneToOneField(Post, related_name = 'post_comment', on_delete = models.CASCADE, validators=[validate_status])
    author = models.ForeignKey(User,related_name = 'comment_author', on_delete=models.CASCADE)
    body   = models.TextField();
    created =  models.DateTimeField(auto_now_add =True)
    
    def __str__(self):
        return str(self.post.status)



class Like(models.Model):
    post    =   models.ForeignKey(Post, related_name = 'liked_post', on_delete = models.CASCADE)
    author  =   models.ForeignKey(User, related_name= 'author_like',on_delete =models.CASCADE)
    created =   models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
        

class Dislike(models.Model):
    post    =   models.OneToOneField(Post, related_name = 'disliked_post', on_delete = models.CASCADE)
    author  =   models.ManyToManyField(User, related_name= 'author_dislike')
    created =   models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return str(self.post.id)




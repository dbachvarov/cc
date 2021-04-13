from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from .models import Like, Dislike
#import datetime, pytz
# myapi/serializers.py


class PostSerializer(serializers.ModelSerializer):
	#is_active =serializers.ReadOnlyField()
	is_active = serializers.ReadOnlyField()
	class Meta:
		model =	Post
		#fields = ('id','title','author','topic','body','status', 'expiration_time','is_active')
		fields =('id','title','expiration_time','is_active','status')
	
		

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('post','author', 'body', 'created')

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Like
		fields = ('post', 'author','created')

class DislikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dislike
		fields = ('post','author','created')
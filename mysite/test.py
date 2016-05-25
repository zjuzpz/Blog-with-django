from django.contrib.auth.models import User
from blog.models import Post


#Test
Post.published.filter(title__startwith = 'first')

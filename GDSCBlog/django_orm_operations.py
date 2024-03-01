import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment

# For Posts
# Create at least 3 posts
Post.objects.create(title='First Post', content='Content for the first post.', category='Technology', tags=['tech'])
Post.objects.create(title='Second Post', content='Content for the second post.', category='Food', tags=['food'])
Post.objects.create(title='Third Post', content='Content for the third post.', category='Travel', tags=['travel'])

# Query and display all posts in a specific category
posts_in_tech_category = Post.objects.filter(category='Technology')
for post in posts_in_tech_category:
    print(post.title, post.content)

# Update the content of one of the posts
post_to_update = Post.objects.get(title='First Post')
post_to_update.content = 'Updated content for the first post.'
post_to_update.save()

# Delete a post
Post.objects.filter(title='Third Post').delete()

# For Comments
# Create at least 3 comments related to different blog posts
post = Post.objects.get(title='First Post')
Comment.objects.create(content='First comment on the first post.', author='Alice', published_date='2024-02-29', post=post)
Comment.objects.create(content='Second comment on the first post.', author='Bob', published_date='2024-02-29', post=post)

# Query and display all comments related to a specific post
comments_for_first_post = Comment.objects.filter(post=post)
for comment in comments_for_first_post:
    print(comment.content, comment.author)

# Update the content of one of the comments
comment_to_update = Comment.objects.get(author='Alice')
comment_to_update.content = 'Updated comment from Alice.'
comment_to_update.save()

# Delete a comment
Comment.objects.filter(author='Bob').delete()

from django.db import models
from django.contrib.auth.models import User

# user0 = User.objects.all()[0]
# user1 = User.objects.all()[1]
# Follow.objects.create(from_user=user1, to_user=user0)
# user0.followers.all()[0].from_user
# user1.following.all()[0].to_user

class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('from_user', 'to_user')


class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def comments_with_posters(self):
        return self.comment_set.select_related('poster')


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at', )

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

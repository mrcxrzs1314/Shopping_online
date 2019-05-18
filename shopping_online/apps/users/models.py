from django.contrib.auth.models import AbstractUser, UserManager as _UserManager


class UserManager(_UserManager):

    def create_superuser(self, username, password, email=None, **extra_fields):
        super(UserManager, self).create_superuser(username=username,
                                                  password=password, email=email, **extra_fields)


class Users(AbstractUser):

    objects = UserManager()

    class Meta:
        db_table = "users_users"   # 指明数据库表名

    def __str__(self):  # 打印对象时调用
        return self.username

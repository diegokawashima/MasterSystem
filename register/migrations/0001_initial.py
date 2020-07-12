# Generated by Django 3.0.3 on 2020-07-05 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import register.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', register.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_name', models.CharField(max_length=100, verbose_name='＜講師＞')),
                ('lecture_email', models.EmailField(max_length=100, verbose_name='講師メール')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30, verbose_name='科目')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='動画タイトル')),
                ('description', models.TextField(blank=True, verbose_name='説明(空欄可)')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='サムネイル(空欄可)')),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='ファイル')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('count', models.IntegerField(default=0, verbose_name='再生回数')),
                ('comment_count', models.IntegerField(default=0, verbose_name='コメント数')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Subject', verbose_name='科目')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='＜タイトル＞')),
                ('text', models.TextField(verbose_name='＜コメント＞')),
                ('reply_image1', models.ImageField(blank=True, null=True, upload_to='reply_images/', verbose_name='＜画像1を投稿する＞')),
                ('reply_image2', models.ImageField(blank=True, null=True, upload_to='reply_images/', verbose_name='＜画像2を投稿する＞')),
                ('reply_image3', models.ImageField(blank=True, null=True, upload_to='reply_images/', verbose_name='＜画像3を投稿する＞')),
                ('reply_video', models.FileField(blank=True, null=True, upload_to='reply_videos/%Y/%m/%d/', verbose_name='＜動画でコメントする＞')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='＜投稿日時＞')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Lecturer', verbose_name='講師')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Video', verbose_name='紐づく記事')),
            ],
        ),
    ]
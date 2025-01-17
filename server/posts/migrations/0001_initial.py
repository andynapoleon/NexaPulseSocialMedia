# Generated by Django 5.0.1 on 2024-03-22 02:26

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('type', models.CharField(default='post', editable=False, max_length=4)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'Public'), ('FRIENDS', 'Friends'), ('UNLISTED', 'Unlisted')], default=('PUBLIC', 'Public'), max_length=20)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('contentType', models.CharField(choices=[('text/plain', 'plain'), ('text/markdown', 'markdown'), ('image/png;base64', 'png'), ('image/jpeg;base64', 'jpeg')], default='text/plain', max_length=20)),
                ('content', models.TextField(default='')),
                ('originalContent', models.TextField(default='')),
                ('isShared', models.BooleanField(default=False)),
                ('authorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('image_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post')),
                ('sharedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shared_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

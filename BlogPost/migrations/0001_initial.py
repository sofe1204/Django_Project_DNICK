# Generated by Django 4.0.5 on 2022-06-04 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('files', models.FileField(max_length=254, upload_to=None)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_content', models.TextField(blank=True, null=True)),
                ('blog_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogPost.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostCommentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogPost.user')),
                ('blogPost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogPost.blogpost')),
                ('commentar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogPost.commentar')),
            ],
        ),
    ]

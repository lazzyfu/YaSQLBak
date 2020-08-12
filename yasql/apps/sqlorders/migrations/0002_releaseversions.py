# Generated by Django 3.1 on 2020-08-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseVersions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('username', models.CharField(default='', max_length=128, verbose_name='创建用户')),
                ('version', models.CharField(default='', max_length=128, unique=True, verbose_name='版本号')),
                ('expire_time', models.DateTimeField(auto_now_add=True, verbose_name='截止上线日期')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '工单发布版本号',
                'verbose_name_plural': '工单发布版本号',
                'db_table': 'yasql_release_versions',
                'default_permissions': (),
            },
        ),
    ]

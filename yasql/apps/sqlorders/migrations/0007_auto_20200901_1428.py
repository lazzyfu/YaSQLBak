# Generated by Django 3.1 on 2020-09-01 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0006_auto_20200812_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dborders',
            name='immediate_execute_reason',
        ),
        migrations.RemoveField(
            model_name='dborders',
            name='window_time',
        ),
        migrations.AddField(
            model_name='dborders',
            name='is_hide',
            field=models.CharField(blank=True, default='OFF', max_length=10, verbose_name='是否隐藏'),
        ),
        migrations.CreateModel(
            name='DbExportFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('file_name', models.CharField(default='', max_length=200, unique=True, verbose_name='文件名')),
                ('file_size', models.IntegerField(default=0, verbose_name='文件大小，单位B')),
                ('files', models.FileField(upload_to='export/')),
                ('encryption_key', models.CharField(default='', max_length=128, verbose_name='加密密钥')),
                ('content_type', models.CharField(default='', max_length=100, verbose_name='文件的类型')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sqlorders.dbordersexecutetasks', verbose_name='关联执行任务的主键id')),
            ],
            options={
                'verbose_name': 'DB导出文件',
                'verbose_name_plural': 'DB导出文件',
                'db_table': 'yasql_sqlorders_export_files',
                'default_permissions': (),
            },
        ),
    ]

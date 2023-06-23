# Generated by Django 3.1.14 on 2022-11-23 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_added_post_vote_model'),
        ('reports', '0002_user_report_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.TextField(blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('INITIATED', 'Initiated'), ('VERIFIED', 'Verified'), ('RESOLVED', 'Resolved'), ('REJECTED', 'Rejected'), ('REDACTED', 'Redacted')], default='INITIATED', help_text='\n        1. Anyone can create a report. Does not mean it is valid\n        2. Report is valid and further actions can be taken.\n        3. The Report was verified but is no longer valid. The problem has been solved.\n        4. Verified and found the report has no basis. Fake/ Invalid.\n        5. User is withdrawing the report.\n    ', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='posts.post')),
                ('report_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postreport_reports', to='reports.reporttype')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postreport_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post Report',
                'verbose_name_plural': 'Post Reports',
                'ordering': ['-created_at'],
            },
        ),
    ]

# Generated by Django 2.2.16 on 2020-11-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0033_dont_cascade_delete_builds'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionautomationrule',
            name='on_match',
            field=models.BooleanField(default=True, help_text="Perform this action when the pattern matches or when it doesn't match?", null=True, verbose_name='Perform action on match?'),
        ),
    ]
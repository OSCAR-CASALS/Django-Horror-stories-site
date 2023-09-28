# Generated by Django 4.2.4 on 2023-09-27 12:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('title_and_user', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('story', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': [django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('likes'), '-', models.F('dislikes')), '*', models.Value(-1))],
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=200)),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SearchAndReadApp.story')),
            ],
        ),
    ]
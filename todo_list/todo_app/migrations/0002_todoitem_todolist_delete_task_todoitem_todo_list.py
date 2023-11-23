# Generated by Django 4.2.7 on 2023-11-23 18:44

from django.db import migrations, models
import django.db.models.deletion
import todo_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(default=todo_app.models.one_week_hence)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todolist'),
        ),
    ]
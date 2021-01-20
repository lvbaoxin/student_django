# Generated by Django 3.1.5 on 2021-01-20 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.clazz')),
                ('cour', models.ManyToManyField(to='stu.Course')),
            ],
        ),
    ]
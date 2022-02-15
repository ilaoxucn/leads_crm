# Generated by Django 3.2.4 on 2021-07-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('BMW', 'BMW Bao Ma'), ('AUDI', 'Audi card'), ('Ferrari', 'Ferrari car')], max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=2015)),
            ],
        ),
    ]
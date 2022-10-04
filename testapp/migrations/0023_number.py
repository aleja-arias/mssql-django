# Generated by Django 4.0.7 on 2022-09-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0022_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.BigIntegerField(db_column='the_integer')),
                ('float', models.FloatField(db_column='the_float', null=True)),
                ('decimal_value', models.DecimalField(decimal_places=17, max_digits=20, null=True)),
            ],
        ),
    ]
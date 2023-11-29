

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='producat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='seller',
            name='address',
            field=models.CharField(default='Vincent', max_length=150),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(default='Masyuko', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(default='0790949144'),
        ),
    ]

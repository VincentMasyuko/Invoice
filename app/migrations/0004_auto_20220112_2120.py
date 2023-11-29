from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producat_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='address',
            field=models.CharField(default='Sultan Hamud', max_length=150),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(default='Vincent Masyuko', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(default='0790949144'),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220112_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='producat',
            name='img',
            field=models.ImageField(default='', upload_to='media/'),
            preserve_default=False,
        ),
    ]

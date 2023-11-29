
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220112_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='seller',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

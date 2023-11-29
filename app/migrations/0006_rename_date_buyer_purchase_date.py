from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220112_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='date',
            new_name='purchase_date',
        ),
    ]

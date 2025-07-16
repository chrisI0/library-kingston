from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_add_shelf_level_column_to_bookdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='date_borrowed',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

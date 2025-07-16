from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_add_date_borrowed_to_borrow'),
        ('app1', '0008_remove_bookdetails_address'),
    ]

    operations = [
        # No operations needed, just merging the dependencies
    ]

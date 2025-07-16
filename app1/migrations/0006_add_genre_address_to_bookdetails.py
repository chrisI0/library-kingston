from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_borrow_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='genre',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='address',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]

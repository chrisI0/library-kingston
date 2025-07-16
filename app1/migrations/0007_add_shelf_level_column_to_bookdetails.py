from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_add_genre_address_to_bookdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='shelf',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='level',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='column',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

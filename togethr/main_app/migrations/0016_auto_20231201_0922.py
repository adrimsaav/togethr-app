from django.db import migrations

def delete_photos(apps, schema_editor):
    Photo = apps.get_model('main_app', 'Photo')
    Photo.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_photo_user_photo_post_alter_post_photo'),
    ]

    operations = [
        migrations.RunPython(delete_photos),
    ]

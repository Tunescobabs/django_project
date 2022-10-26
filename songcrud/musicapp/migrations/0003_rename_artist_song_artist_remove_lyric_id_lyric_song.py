# Generated by Django 4.1.2 on 2022-10-26 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song_artist_alter_song_date_released'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Artist',
            new_name='artist',
        ),
        migrations.RemoveField(
            model_name='lyric',
            name='id',
        ),
        migrations.AddField(
            model_name='lyric',
            name='Song',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='musicapp.song'),
            preserve_default=False,
        ),
    ]

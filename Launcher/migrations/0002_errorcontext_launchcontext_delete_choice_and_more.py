from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LaunchContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_url', models.TextField()),
                ('instance_id', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-20 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freeagency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freeagent',
            name='last_bid_time',
        ),
        migrations.AddField(
            model_name='freeagent',
            name='rfa_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='freeagency.gm'),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_bid', models.IntegerField()),
                ('last_bid_time', models.DateTimeField(auto_now=True)),
                ('last_bid_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeagency.gm')),
            ],
        ),
        migrations.AlterField(
            model_name='freeagent',
            name='last_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeagency.bid'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-05-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gossip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='GossipList',
        ),
    ]

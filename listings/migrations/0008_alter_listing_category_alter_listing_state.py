# Generated by Django 4.2.1 on 2023-05-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Jobs', 'Jobs'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Mobiles', 'Mobiles'), ('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Bikes', 'Bikes'), ('Cars', 'Cars')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('AP', 'Andhra Pradesh'), ('UP', 'Uttar Pradesh'), ('PB', 'Punjab'), ('GA', 'Goa'), ('WB', 'West Bengal'), ('MH', 'Maharashtra'), ('ML', 'Meghalaya'), ('CG', 'Chhattisgarh'), ('HP', 'Haryana'), ('TN', 'Tamil Nadu'), ('MI', 'Sikkim'), ('MP', 'Madhya Pradesh'), ('TR', 'Tripura'), ('GJ', 'Gujarat'), ('NL', 'Nagaland'), ('JH', 'Jharkhand'), ('TS', 'Telegana'), ('BR', 'Bihar'), ('AR', 'Arunachal Pradesh'), ('OD', 'Odisha'), ('MN', 'Manipur'), ('UK', 'Uttarakhand'), ('KA', 'Karnataka'), ('MZ', 'Mizoram'), ('AS', 'Assam'), ('KL', 'Kerala'), ('RJ', 'Rajasthan')], max_length=100),
        ),
    ]

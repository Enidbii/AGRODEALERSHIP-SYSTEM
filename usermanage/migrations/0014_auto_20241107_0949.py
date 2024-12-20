# Generated by Django 5.1.2 on 2024-11-07 06:49

from django.db import migrations

def create_groups(apps, schema_migration):
    User = apps.get_model('usermanage', 'OtherUser')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_employee = Permission.objects.get(codename='add_employee')
    change_employee = Permission.objects.get(codename='change_employee')
    delete_employee = Permission.objects.get(codename='delete_employee')
    view_employee = Permission.objects.get(codename='view_employee')

    admin_permissions = [
        add_employee,
        change_employee,
        delete_employee,
        view_employee,
    ]

    admins = Group(name='admin')
    admins.save()

    admins.permissions.set(admin_permissions)

    finance = Group(name='finance')
    finance.save()
    finance.permissions.add(view_employee)


    for user in User.objects.all():
        if user.groups == 'ADMIN':
            admins.user_set.add(user)
        if user.groups == 'FINANCE':
            finance.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0013_alter_corporate_status'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]


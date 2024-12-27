from django.db import migrations

def add_initial_players(apps, schema_editor):
    Player = apps.get_model('rankings', 'Player')
    
    players_data = [
        # G8 Boys
        {'first_name': 'Mike', 'last_name': 'Xu', 'grade_level': 'G8 Boys'},
        {'first_name': 'Eddie', 'last_name': 'Chao', 'grade_level': 'G8 Boys'},
        {'first_name': 'Devin', 'last_name': 'Wu', 'grade_level': 'G8 Boys'},
        {'first_name': 'Kevin', 'last_name': 'Li', 'grade_level': 'G8 Boys'},
        {'first_name': 'Luke', 'last_name': 'Guo', 'grade_level': 'G8 Boys'},
        {'first_name': 'DONOVAN', 'last_name': 'LIN', 'grade_level': 'G8 Boys'},
        {'first_name': 'KEVIN', 'last_name': 'WANG', 'grade_level': 'G8 Boys'},
        {'first_name': 'Felix', 'last_name': 'Yang', 'grade_level': 'G8 Boys'},
        {'first_name': 'Dale', 'last_name': 'Yang', 'grade_level': 'G8 Boys'},

        # G8 Girls
        {'first_name': 'Olivia', 'last_name': 'Li', 'grade_level': 'G8 Girls'},
        {'first_name': 'Grace', 'last_name': 'Liu', 'grade_level': 'G8 Girls'},
        {'first_name': 'Sophia', 'last_name': 'Ge', 'grade_level': 'G8 Girls'},
        {'first_name': 'Olivia', 'last_name': 'WU', 'grade_level': 'G8 Girls'},
        {'first_name': 'Catherine', 'last_name': 'Ming', 'grade_level': 'G8 Girls'},
        {'first_name': 'Chloe', 'last_name': 'Yu', 'grade_level': 'G8 Girls'},
        {'first_name': 'Ava', 'last_name': 'Tian', 'grade_level': 'G8 Girls'},
        {'first_name': 'Felix', 'last_name': 'Wu', 'grade_level': 'G8 Girls'},
        {'first_name': 'Jessie', 'last_name': 'Guo', 'grade_level': 'G8 Girls'},
        {'first_name': 'Momo', 'last_name': 'Li', 'grade_level': 'G8 Girls'},
        {'first_name': 'Bella', 'last_name': 'Sun', 'grade_level': 'G8 Girls'},
        {'first_name': 'Misaki', 'last_name': 'Tea', 'grade_level': 'G8 Girls'},

        # Junior Boys
        {'first_name': 'George', 'last_name': 'Xue', 'grade_level': 'Junior Boys'},
        {'first_name': 'Reaky', 'last_name': 'Fang', 'grade_level': 'Junior Boys'},
        {'first_name': 'Ryan', 'last_name': 'Yu', 'grade_level': 'Junior Boys'},
        {'first_name': 'Greg', 'last_name': 'Li', 'grade_level': 'Junior Boys'},
        {'first_name': 'Mingkai', 'last_name': 'Yu', 'grade_level': 'Junior Boys'},
        {'first_name': 'Ethan', 'last_name': 'Liu', 'grade_level': 'Junior Boys'},
        {'first_name': 'Kevin', 'last_name': 'Wu', 'grade_level': 'Junior Boys'},
        {'first_name': 'Rephael', 'last_name': 'Zhang', 'grade_level': 'Junior Boys'},
        {'first_name': 'Richard', 'last_name': 'Zhou', 'grade_level': 'Junior Boys'},

        # Junior Girls
        {'first_name': 'Jolene', 'last_name': 'Zhang', 'grade_level': 'Junior Girls'},
        {'first_name': 'Abigail', 'last_name': 'Fu', 'grade_level': 'Junior Girls'},
        {'first_name': 'Yuki', 'last_name': 'Sun', 'grade_level': 'Junior Girls'},
        {'first_name': 'Jocelyn', 'last_name': 'LI', 'grade_level': 'Junior Girls'},
        {'first_name': 'Eleanor', 'last_name': 'Fu', 'grade_level': 'Junior Girls'},
        {'first_name': 'Aimee', 'last_name': 'Wang', 'grade_level': 'Junior Girls'},
        {'first_name': 'Aurora', 'last_name': 'Yu', 'grade_level': 'Junior Girls'},
        {'first_name': 'Rosanna', 'last_name': 'Lin', 'grade_level': 'Junior Girls'},
        {'first_name': 'Angelica', 'last_name': 'Wang', 'grade_level': 'Junior Girls'},
        {'first_name': 'Isabella', 'last_name': 'Shang', 'grade_level': 'Junior Girls'},
        {'first_name': 'Alysia', 'last_name': 'Wen', 'grade_level': 'Junior Girls'},
        {'first_name': 'Chloe', 'last_name': 'Kuo', 'grade_level': 'Junior Girls'},
        {'first_name': 'Amanda', 'last_name': 'Shen', 'grade_level': 'Junior Girls'},
        {'first_name': 'jacqueline', 'last_name': 'lin', 'grade_level': 'Junior Girls'},

        # Senior Boys
        {'first_name': 'Rickey', 'last_name': 'Zhang', 'grade_level': 'Senior Boys'},
        {'first_name': 'Michael', 'last_name': 'Du', 'grade_level': 'Senior Boys'},
        {'first_name': 'William', 'last_name': 'Lee', 'grade_level': 'Senior Boys'},
        {'first_name': 'Frank', 'last_name': 'Wang', 'grade_level': 'Senior Boys'},
        {'first_name': 'Samuel', 'last_name': 'Li', 'grade_level': 'Senior Boys'},
        {'first_name': 'Ryan', 'last_name': 'Cao', 'grade_level': 'Senior Boys'},
        {'first_name': 'Collin', 'last_name': 'Yang', 'grade_level': 'Senior Boys'},
        {'first_name': 'Andy', 'last_name': 'Zhang', 'grade_level': 'Senior Boys'},
        {'first_name': 'John', 'last_name': 'Gao', 'grade_level': 'Senior Boys'},

        # Senior Girls
        {'first_name': 'Xue', 'last_name': 'Yan', 'grade_level': 'Senior Girls'},
        {'first_name': 'Ingrid', 'last_name': 'Yang', 'grade_level': 'Senior Girls'},
        {'first_name': 'Amy', 'last_name': 'Wu', 'grade_level': 'Senior Girls'},
        {'first_name': 'Ruth', 'last_name': 'Li', 'grade_level': 'Senior Girls'},
        {'first_name': 'Nicole', 'last_name': 'Wang', 'grade_level': 'Senior Girls'},
        {'first_name': 'Joy', 'last_name': 'Feng', 'grade_level': 'Senior Girls'},
    ]
    
    for player in players_data:
        Player.objects.create(**player)

def remove_players(apps, schema_editor):
    Player = apps.get_model('rankings', 'Player')
    Player.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('rankings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_players, remove_players),
    ] 
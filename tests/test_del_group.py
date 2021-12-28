import random


def test_del_group(app):
    old_list = app.group.get_group_list()
    random_group = random.choice(old_list)
    app.group.del_some_group(random_group)
    new_list = app.group.get_group_list()
    old_list.remove(random_group)
    assert sorted(old_list) == sorted(new_list)

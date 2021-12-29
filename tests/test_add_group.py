def test_add_group(app, xlsx_groups):
    new_group = xlsx_groups
    old_list = app.group.get_group_list()
    app.group.add_new_group(new_group)
    new_list = app.group.get_group_list()
    if new_group == "":
        old_list += ["New group"]
    else:
        old_list += [new_group]
    assert sorted(old_list) == sorted(new_list)

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def del_some_group(self, group_name):
        self.open_group_editor()
        self.group_editor.window(title=group_name).click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_del_window = self.app.application.window(title="Delete group")  # сохраняем ссылку на модальное окно подтверждения удаления
        self.group_del_window.wait("visible")
        self.group_del_window.window(auto_id="uxOKAddressButton").click()


    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()  # нажимаем на кнопку для вызова модального окна редактирования групп
        self.group_editor = self.app.application.window(title="Group editor")  # сохраняем ссылку на модальное окно
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

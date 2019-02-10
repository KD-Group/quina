from PySide2.QtWidgets import QMessageBox


class MessageBoxInterface:
    def question(self, text, title='选择'):
        # noinspection PyCallByClass
        return QMessageBox.question(self, title, text, QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes

    def warning(self, text, title='警告'):
        # noinspection PyCallByClass
        QMessageBox.warning(self, title, text)

    def information(self, text, title='提示'):
        # noinspection PyCallByClass
        QMessageBox.information(self, title, text)

    def about(self, text, title='关于'):
        # noinspection PyCallByClass
        QMessageBox.about(self, title, text)

    def message(self, ok=True, ok_msg='成功', bad_msg='失败'):
        if ok:
            self.information(ok_msg)
        else:
            self.warning(bad_msg)

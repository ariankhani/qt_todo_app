import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QDialog,
    QMessageBox,
)
from PySide6.QtCore import Qt
from typing import Sequence
from persiantools.jdatetime import JalaliDate
from datetime import datetime

from ui.my_todo import Ui_MainWindow
from ui.add_todo import Ui_AddTodo
from ui.set_size import Ui_set_size

from ui.db.todo_database import Todo, get_todo, add_todo, delete_todo, update_todo


class TodoAddDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.ui = Ui_AddTodo()
        self.ui.setupUi(self)

        # Connect butten
        self.ui.ok_cancel_btn.accepted.connect(self.accept)
        self.ui.ok_cancel_btn.rejected.connect(self.reject)

    def get_todo_data(self):
        todo_data = {
            "name": self.ui.add_name_inp.text(),
            "status": self.ui.checkBox.isChecked(),
            "description": self.ui.add_description_inp.toPlainText(),
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Automatically fill the date
        }
        return todo_data


class TodoSetSize(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.set_size = Ui_set_size()
        self.set_size.setupUi(self)

        self.set_size.buttonBox.accepted.connect(self.accept)
        self.set_size.buttonBox.rejected.connect(self.reject)

    def get_size(self):
        # Get text from the input fields
        width_text = self.set_size.lengt_inp.text()
        height_text = self.set_size.heigh_inp.text()

        width = int(width_text)
        height = int(height_text)

        # Check if the inputs are numeric
        if not width_text.isdigit() or not height_text.isdigit():
            QMessageBox.warning(
                parent=self,
                title="Invalid Input",
                text="Please enter numeric values for width and height.",
            )
            return  # Do not proceed if inputs are invalid

        if width <= 450 or height <= 350:
            QMessageBox.warning(
                parent=self, title="Invalid Input", text=f"Width and height must be positive numbers width: {width} and height: {height}."
            )
            return

        # Accept the dialog if all validations pass
        self.accept()

        return width, height


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, width, height) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Todo App")

        # Set the main window size
        self.resize(width, height)


class TodoApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_id: int = -1
        self.setup_table()
        self.signals()

        self.resize(width, height)

    def setup_table(self):
        """Setup table for show on ui"""
        header = ["وضعیت", "اسم", "تاریخ", "توضیحات"]
        self.Todo_list.setHorizontalHeaderLabels(header)

    def signals(self):
        """Add coniction for ui to ux"""
        self.Todo_list.itemSelectionChanged.connect(self.item_selected)
        self.Add_todo.clicked.connect(self.open_todo_dialog)
        self.Update_todo.clicked.connect(self.update_todo)
        self.Delete_todo.clicked.connect(self.delete_todos)
        self.load_todos()

    def load_todos(self, todo: Sequence[Todo] | None = None):
        if not todo:
            todo = get_todo()
        self.Todo_list.setRowCount(len(todo))

        for row_index, todos in enumerate(todo):
            status_item = QTableWidgetItem("انجام شده" if todos.status else "انجام نشده")
            name_item = QTableWidgetItem(todos.name)
            date_item = QTableWidgetItem(
                str(JalaliDate.to_jalali(todos.date_added).strftime("%Y-%m-%d"))
            )
            description_item = QTableWidgetItem(todos.description)

            # Set the ID as UserRole data for the name item (or another item if preferred)
            name_item.setData(Qt.UserRole, todos.id)

            self.Todo_list.setItem(row_index, 0, status_item)
            self.Todo_list.setItem(row_index, 1, name_item)
            self.Todo_list.setItem(row_index, 2, date_item)
            self.Todo_list.setItem(row_index, 3, description_item)

    def add_todo(self):
        """This Function use for add new"""
        name = self.TodoName.text()
        description = self.TodoDescription.text()
        status = self.TodoStatus.isChecked()
        if not name or not description:
            QMessageBox.warning(
                parent=self, title="Missing Information", text="Please provide both name and description."
            )
            return

        todo = Todo(name=name, description=description, status=status)
        add_todo(todo)
        self.load_todos()
        self.TodoName.clear()
        self.TodoDescription.clear()
        self.TodoStatus.setChecked(False)

    def item_selected(self):
        selected_items = self.Todo_list.selectedItems()
        if selected_items and len(selected_items) >= 4:
            # Get the Todo ID from the selected row
            self.selected_id = selected_items[1].data(Qt.UserRole)
            self.TodoName.setText(selected_items[1].text())
            self.TodoDescription.setText(selected_items[3].text())
            self.TodoStatus.setChecked(selected_items[0].text() == "Done")
        else:
            self.selected_id = -1

    def update_todo(self):
        name = self.TodoName.text()
        description = self.TodoDescription.text()
        if not name or not description or self.selected_id == -1:
            QMessageBox.warning(
                parent=self,
                title="Missing Information",
                text="Please select a todo and provide all the information.",
            )
            return

        todo = Todo(
            id=self.selected_id,
            name=name,
            description=description,
            status=self.TodoStatus.isChecked(),
        )
        update_todo(todo)
        self.load_todos()

    def delete_todos(self):
        if self.selected_id is None:
            QMessageBox.warning(
                parent=self, title="Missing Information", text="Please select a todo to delete."
            )
            return

        ans = QMessageBox()
        ans.setText("Are you sure you want to delete this todo?")
        ans.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        response = ans.exec()

        if response == QMessageBox.StandardButton.Yes:
            delete_todo(self.selected_id)  # Call the delete_todo function
            self.load_todos()  # Reload or refresh the UI table after deletion

            # Clear the input fields and reset the selected_id after deletion
            self.TodoName.clear()
            self.TodoDescription.clear()
            self.TodoStatus.setChecked(False)
            self.selected_id = None

    def open_todo_dialog(self):
        dialog = TodoAddDialog(self)
        if dialog.exec():
            todo_data = dialog.get_todo_data()
            if todo_data["name"]:
                self.add_todo_to_list(todo_data)
            else:
                QMessageBox.warning(parent=self, title="Warning", text="Name cannot be empty")

    def add_todo_to_list(self, todo_data):
        todo = Todo(
            name=todo_data["name"],
            description=todo_data["description"],
            status=todo_data["status"],
        )
        add_todo(todo)
        self.load_todos()
        self.TodoName.clear()
        self.TodoDescription.clear()
        self.TodoStatus.setChecked(False)

    def run(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    size_dialog = TodoSetSize()

    if size_dialog.exec() == QDialog.Accepted:
        width, height = size_dialog.get_size()

        window = MainWindow(width, height)

        ui = TodoApp()
        ui.run()

    sys.exit(app.exec())

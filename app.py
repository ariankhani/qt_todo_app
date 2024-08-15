import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    # QWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt
from typing import Sequence
from persiantools.jdatetime import JalaliDate
from ui.my_todo import Ui_MainWindow
from ui.db.todo_database import Todo, get_todo, add_todo, delete_todo, update_todo


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)


class TodoApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_id: int = -1
        self.setup_table()
        self.signals()

    def setup_table(self):
        """Setup table for show on ui"""
        header = ["Status", "Name", "Date", "Description"]
        self.Todo_list.setHorizontalHeaderLabels(header)

    def signals(self):
        """Add coniction for ui to ux"""
        self.Todo_list.itemSelectionChanged.connect(self.item_selected)
        self.Add_todo.clicked.connect(self.add_todo)
        self.Update_todo.clicked.connect(self.update_todo)
        self.Delete_todo.clicked.connect(self.delete_todos)
        self.load_todos()

    def load_todos(self, todo: Sequence[Todo] | None = None):
        if not todo:
            todo = get_todo()
        self.Todo_list.setRowCount(len(todo))

        for row_index, todos in enumerate(todo):
            status_item = QTableWidgetItem('Done' if todos.status else "Waiting")
            name_item = QTableWidgetItem(todos.name)
            date_item = QTableWidgetItem(str(JalaliDate.to_jalali(todos.date_added).strftime("%Y-%m-%d")))
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
                self, "Missing Information", "Please provide both name and description."
            )
            return

        todo = Todo(
            name=name, description=description, status=status
        )
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
                self,
                "Missing Information",
                "Please select a todo and provide all the information.",
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
                self, "Missing Information", "Please select a todo to delete."
            )
            return

        ans = QMessageBox()
        ans.setText("Are you sure you want to delete this todo?")
        ans.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        response = ans.exec()

        if response == QMessageBox.StandardButton.Yes:
            delete_todo(self.selected_id)  # Call the delete_todo function
            self.load_todos()  # Reload or refresh the UI table after deletion

            # Clear the input fields and reset the selected_id after deletion
            self.TodoName.clear()
            self.TodoDescription.clear()
            self.TodoStatus.setChecked(False)
            self.selected_id = None


    def run(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = TodoApp()
    ui.run()
    sys.exit(app.exec())

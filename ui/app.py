import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtWidgets import QMessageBox

from persiantools.jdatetime import JalaliDate

from my_todo import Ui_MainWindow
from db.todo_database import (
    get_session,
    Todo,
)


class TodoApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to methods
        self.Todo_list.itemSelectionChanged.connect(self.item_selected)
        self.Add_todo.clicked.connect(self.add_todo)
        self.Update_todo.clicked.connect(self.update_todo)
        self.Delete_todo.clicked.connect(self.delete_todo)

        # Load existing todos
        self.load_todos()

    def load_todos(self):
        """This function displays the entire todo list to the user."""
        self.Todo_list.setRowCount(0)  # Set row in 0 position
        with get_session() as session:
            todos = session.query(Todo).all()
            for todo in todos:
                row_position = self.Todo_list.rowCount()
                self.Todo_list.insertRow(row_position)

                # Set table item
                self.Todo_list.setItem(
                    row_position,
                    0,
                    QTableWidgetItem("Done" if todo.status else "Waiting"),
                )

                self.Todo_list.setItem(row_position, 1, QTableWidgetItem(todo.name))

                # jalali_date = JalaliDate.to_jalali(todo.date_added)
                self.Todo_list.setItem(
                    row_position,
                    2,
                    QTableWidgetItem(JalaliDate.to_jalali(todo.date_added).strftime("%y-%m-%d")),
                )

                self.Todo_list.setItem(
                    row_position, 3, QTableWidgetItem(todo.description)
                )

    def add_todo(self):
        """This Function for Add a new todo to list"""
        name = self.TodoName.text()
        description = self.TodoDescription.text()
        status = self.TodoStatus.isChecked()

        missing_fields = []

        if not name:
            missing_fields.append("Name")
        if not description:
            missing_fields.append("Description")

        if missing_fields:
            missing_fields_str = ", ".join(missing_fields)
            QMessageBox.warning(
                self, "Empty Fields", f"Please fill in the following fields: {missing_fields_str}."
            )
        else:
            with get_session() as session:
                new_todo = Todo(name=name, description=description, status=status)
                session.add(new_todo)
                session.commit()
            self.load_todos()


    def item_selected(self):
        """This Function for find out witch item selected"""
        selected_items = self.Todo_list.selectedItems()
        if selected_items:
            name = selected_items[1].text()
            with get_session() as session:
                selected_todo = session.query(Todo).filter_by(name=name).first()
                if selected_todo:
                    self.TodoName.setText(selected_todo.name)
                    self.TodoDescription.setText(selected_todo.description)
                    self.TodoStatus.setChecked(selected_todo.status)

    def update_todo(self):
        """Update selected Todo"""
        selected_items = self.Todo_list.selectedItems()
        if selected_items:
            name = selected_items[1].text()
            with get_session() as session:
                selected_todo = session.query(Todo).filter_by(name=name).first()
                if selected_todo:
                    selected_todo.name = self.TodoName.text()
                    selected_todo.description = self.TodoDescription.text()
                    selected_todo.status = self.TodoStatus.isChecked()
                    session.commit()
            self.load_todos()

    def delete_todo(self):
        """Delete selected Todo"""
        selected_items = self.Todo_list.selectedItems()
        if selected_items:
            name = selected_items[1].text()
            with get_session() as session:
                selected_todo = session.query(Todo).filter_by(name=name).first()
                if selected_todo:
                    session.delete(selected_todo)
                    session.commit()
            self.load_todos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

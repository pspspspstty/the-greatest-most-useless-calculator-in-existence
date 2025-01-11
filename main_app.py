import sys
import operations
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QDialog, QGridLayout, QLabel,
    QPushButton, QHBoxLayout, QWidget, QLineEdit, QGroupBox, QVBoxLayout
)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.topLeftGroupBox = None
        self.originalPalette = QApplication.palette()
        sys.argv += ['-platform', 'windows:darkmode=1']

        # ComboBox for selecting operations
        self.operation_list = QComboBox()
        self.operation_list.addItems(operations.__all__)
        self.operation_list.currentIndexChanged.connect(self.change_layout)

        operation_list_label = QLabel("&Operation:")
        operation_list_label.setBuddy(self.operation_list)

        # Horizontal layout for operation selector
        top_layout = QHBoxLayout()
        top_layout.addWidget(operation_list_label)
        top_layout.addWidget(self.operation_list)
        top_layout.addStretch(1)  # Push widgets to the left

        # Main layout
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        self.setWindowTitle("Dynamic Layout Example")

        # Add top layout to main layout
        self.main_layout.addLayout(top_layout, 0, 0, 1, 2)

        # Dynamic area for layout switching
        self.dynamic_widget = QWidget()
        self.dynamic_layout = QGridLayout(self.dynamic_widget)
        self.main_layout.addWidget(self.dynamic_widget, 1, 0, 1, 2)

        # Create and store layouts for options
        self.layout_options = self.create_layouts()

        # Add all layouts to the dynamic area (hidden by default)
        self.layout_widgets = {}
        for index, layout in self.layout_options.items():
            widget = QWidget()
            widget.setLayout(layout)
            widget.setVisible(False)
            self.layout_widgets[index] = widget
            self.dynamic_layout.addWidget(widget, 0, 0)

        # Set the initial layout
        self.change_layout(0)

    def create_layouts(self):
        """Create and store layouts for each operation."""
        layouts = {}

        # Layout for Option 1
        self.topLeftGroupBox = QGroupBox("test")

        layout1 = QVBoxLayout()

        layout1.addWidget(QLabel("Vector field:     "))

        x_input = QLineEdit()
        x_input.setPlaceholderText("x-component")
        y_input = QLineEdit()
        y_input.setPlaceholderText("y-component")
        z_input = QLineEdit()
        z_input.setPlaceholderText("z-component")

        fixed_height = 22  # Adjust height as needed
        x_input.setFixedHeight(fixed_height)
        y_input.setFixedHeight(fixed_height)
        z_input.setFixedHeight(fixed_height)

        layout1.addWidget(x_input)
        layout1.addWidget(y_input)
        layout1.addWidget(z_input)

        self.topLeftGroupBox.setLayout(layout1)

        layouts[0] = layout1

        # Layout for Option 2
        layout2 = QGridLayout()
        layout2.addWidget(QLabel("Option 2: Configure settings"), 0, 0)
        layout2.addWidget(QPushButton("Run Option 2"), 1, 0)
        layouts[1] = layout2

        # Layout for Option 3
        layout3 = QGridLayout()
        layout3.addWidget(QLabel("Option 3: Review output"), 0, 0)
        layout3.addWidget(QPushButton("Analyze Option 3"), 1, 0)
        layouts[2] = layout3

        return layouts

    def change_layout(self, index):
        """Switch the layout dynamically based on the selected index."""
        # Hide all layout widgets
        for widget in self.layout_widgets.values():
            widget.setVisible(False)

        # Show the selected layout widget
        if index in self.layout_widgets:
            self.layout_widgets[index].setVisible(True)


def main():
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")
    window = WidgetGallery()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

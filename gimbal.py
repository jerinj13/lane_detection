import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider

class GimbalView(QWidget):
    def __init__(self):
        super().__init__()
        self.pitch_angle = 0
        self.yaw_angle = 0
        self.roll_angle = 0
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw base
        painter.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(200, 200, 200), Qt.SolidPattern))
        painter.drawEllipse(0, 0, self.width(), self.height())

        # Draw pitch
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.pitch_angle, Qt.XAxis)
        painter.setPen(QPen(QColor(255, 0, 0), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(255, 0, 0), Qt.SolidPattern))
        painter.drawEllipse(-self.width() / 8, -self.height() / 8, self.width() / 4, self.height() / 4)
        painter.restore()

        # Draw yaw
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.yaw_angle, Qt.YAxis)
        painter.setPen(QPen(QColor(0, 255, 0), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(0, 255, 0), Qt.SolidPattern))
        painter.drawEllipse(-self.width() / 8, -self.height() / 8, self.width() / 4, self.height() / 4)
        painter.restore()

        # Draw roll
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.roll_angle, Qt.ZAxis)
        painter.setPen(QPen(QColor(0, 0, 255), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(0, 0, 255), Qt.SolidPattern))
        painter.drawEllipse(-self.width() / 8, -self.height() / 8, self.width() / 4, self.height() / 4)
        painter.restore()

        # Draw x
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.x_angle, 1, 0, 0)
        painter.setPen(QPen(QColor(255, 255, 0), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(255, 255, 0), Qt.SolidPattern))
        painter.drawRect(-self.width() / 16, -self.height() / 16, self.width() / 8, self.height() / 8)
        painter.restore()

        # Draw y
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.y_angle, 0, 1, 0)
        painter.setPen(QPen(QColor(255, 255, 0), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(255, 255, 0), Qt.SolidPattern))
        painter.drawRect(-self.width() / 16, -self.height() / 16, self.width() / 8, self.height() / 8)
        painter.restore()

        # Draw z
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.z_angle, 0, 0, 1)
        painter.setPen(QPen(QColor(0, 255, 255), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(0, 255, 255), Qt.SolidPattern))
        painter.drawRect(-self.width() / 16, -self.height() / 16, self.width() / 8, self.height() / 8)
        painter.restore()

    def update_pitch(self, value):
        self.pitch_angle = value
        self.update()

    def update_yaw(self, value):
        self.yaw_angle = value
        self.update()

    def update_roll(self, value):
        self.roll_angle = value
        self.update()

    def update_x(self, value):
        self.x_angle = value
        self.update()

    def update_y(self, value):
        self.y_angle = value
        self.update()

    def update_z(self, value):
        self.z_angle = value
        self.update()

    def main():
        app = QApplication(sys.argv)
        gimbal_view = GimbalView()

    # Create sliders for each axis
    pitch_slider = QSlider(Qt.Horizontal)
    pitch_slider.setMinimum(-90)
    pitch_slider.setMaximum(90)
    pitch_slider.setValue(0)
    pitch_slider.valueChanged.connect(gimbal_view.update_pitch)

    yaw_slider = QSlider(Qt.Horizontal)
    yaw_slider.setMinimum(-90)
    yaw_slider.setMaximum(90)
    yaw_slider.setValue(0)
    yaw_slider.valueChanged.connect(gimbal_view.update_yaw)

    roll_slider = QSlider(Qt.Horizontal)
    roll_slider.setMinimum(-90)
    roll_slider.setMaximum(90)
    roll_slider.setValue(0)
    roll_slider.valueChanged.connect(gimbal_view.update_roll)

    x_slider = QSlider(Qt.Horizontal)
    x_slider.setMinimum(-90)
    x_slider.setMaximum(90)
    x_slider.setValue(0)
    x_slider.valueChanged.connect(gimbal_view.update_x)

    y_slider = QSlider(Qt.Horizontal)
    y_slider.setMinimum(-90)
    y_slider.setMaximum(90)
    y_slider.setValue(0)
    y_slider.valueChanged.connect(gimbal_view.update_y)

    z_slider = QSlider(Qt.Horizontal)
    z_slider.setMinimum(-90)
    z_slider.setMaximum(90)
    z_slider.setValue(0)
    z_slider.valueChanged.connect(gimbal_view.update_z)

    # Create layouts for the sliders and the view
    slider_layout = QVBoxLayout()
    slider_layout.addWidget(QLabel("Pitch"))
    slider_layout.addWidget(pitch_slider)
    slider_layout.addWidget(QLabel("Yaw"))
    slider_layout.addWidget(yaw_slider)
    slider_layout.addWidget(QLabel("Roll"))
    slider_layout.addWidget(roll_slider)
    slider_layout.addWidget(QLabel("X"))
    slider_layout.addWidget(x_slider)
    slider_layout.addWidget(QLabel("Y"))
    slider_layout.addWidget(y_slider)
    slider_layout.addWidget(QLabel("Z"))
    slider_layout.addWidget(z_slider)

    view_layout = QHBoxLayout()
    view_layout.addStretch(1)
    view_layout.addWidget(gimbal_view)
    view_layout.addStretch(1)

    # Combine the layouts into a single main layout
    main_layout = QVBoxLayout()
    main_layout.addLayout(view_layout)
    main_layout.addLayout(slider_layout)

    # Create a widget to hold the main layout
    widget = QWidget()
    widget.setLayout(main_layout)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

if name == 'main':
    main()



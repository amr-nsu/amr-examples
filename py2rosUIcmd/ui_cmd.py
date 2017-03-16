import gtk
import sys
from gettext import gettext as _


class UICmd:
    """UI Class for robot control"""

    velocity = 0.5

    def __init__(self, control, odometry):
        self.control = control
        self.odometry = odometry

        def command_forward(*args):
            self.control.set_vel(UICmd.velocity, 0)
        def command_backward(*args):
            self.control.set_vel(-UICmd.velocity, 0)
        def command_left(*args):
            self.control.set_vel(0, -2 * UICmd.velocity)
        def command_right(*args):
            self.control.set_vel(0,  2 * UICmd.velocity)
        def command_stop(*args):
            self.control.set_vel(0, 0)

        def key_press_callback(widget, event):
            keyval = event.keyval
            if keyval in key_commands.keys():
                key_commands[keyval]()

        def key_release_callback(widget, event):
            command_stop()

        key_commands = {\
                65362: command_forward,
                65364: command_backward,
                65361: command_left,
                65363: command_right,
        }

        window = gtk.Window()
        window.set_title(_('ROS UI Cmd'))
        window.resize(200, 200)
        window.connect('delete-event', self.stop)

        window.connect('key-press-event', key_press_callback)
        window.connect('key-release-event', key_release_callback)

        button_forward = gtk.Button(_('Forward'))
        button_forward.connect('pressed', command_forward)
        button_forward.connect('released', command_stop)

        button_backward = gtk.Button(_('Backward'))
        button_backward.connect('pressed', command_backward)
        button_backward.connect('released', command_stop)

        button_left = gtk.Button(_('Left'))
        button_left.connect('pressed', command_left)
        button_left.connect('released', command_stop)

        button_right = gtk.Button(_('Right'))
        button_right.connect('pressed', command_right)
        button_right.connect('released', command_stop)

        self.label_coordinate = gtk.Label('')

        buttons_hbox = gtk.HBox()
        buttons_hbox.add(button_left)
        buttons_hbox.add(button_right)
        buttons_vbox = gtk.VBox()
        buttons_vbox.add(button_forward)
        buttons_vbox.add(buttons_hbox)
        buttons_vbox.add(button_backward)
        buttons_vbox.add(self.label_coordinate)

        window.add(buttons_vbox)
        window.show_all()

    def coordinates_callback(self, X):
        self.label_coordinate.set_text('x:%4.2f y:%4.2f psi:%4.2f' % X)

    def event_loop(self, *args):
        while gtk.events_pending():
            gtk.main_iteration(block=False)
        return True

    def start(self):
        self.odometry.coordinates_callback = self.coordinates_callback
        self.control.main_loop = self.event_loop
        self.control.start(timeout=0.01)

    def stop(self, *args):
        sys.exit(0)


if __name__ == '__main__':
    from ros_control import ROSControl
    from ros_odometry import ROSOdometry
    control = ROSControl('pioneer2dx')
    odometry = ROSOdometry('pioneer2dx')
    UICmd(control, odometry).start()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hyprand Settings")
        # Header
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Hyprland Settings"

        # Search
        search = Gtk.SearchEntry()
        search.set_placeholder_text('Search Settings')

        # Save
        save = Gtk.Button(label='Save')
        save_style_context = save.get_style_context()
        save_style_context.add_class('suggested-action')

        hb.pack_start(search)
        hb.pack_end(save)
        side_panel = Gtk.StackSidebar()

        grid = Gtk.Grid()
        self.add(grid)

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        grid.attach(stack, 1, 0, 1, 1)

        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        grid.attach(stacksidebar, 0, 0, 1, 1)

        label = Gtk.Label("System details")
        name = "abouts"
        title = "Abouts"
        stack.add_titled(label, name, title)

        label = Gtk.Label("startup commands")
        name = "startup"
        title = "Startup"
        stack.add_titled(label, name, title)

        label = Gtk.Label("Input device")
        name = "input"
        title = "Input"
        stack.add_titled(label, name, title)

        label = Gtk.Label("test")
        stack.add_titled(label, 'test', 'test lol gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay')




        self.set_titlebar(hb)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
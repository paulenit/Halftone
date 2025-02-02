# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk, Adw

from halftone.constants import rootdir


@Gtk.Template(resource_path=f"{rootdir}/ui/preferences_window.ui")
class HalftonePreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = "HalftonePreferencesWindow"

    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)

        self.parent = parent
        self.settings = parent.settings

        self.app = self.parent.get_application()
        self.win = self.app.get_active_window()

        self.set_transient_for(self.win)

        self.setup_signals()
        self.setup()

    def setup_signals(self):
        pass

    def setup(self):
        pass

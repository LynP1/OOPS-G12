class DVD():
    def __init__(self,name,chapters):
        self.name = name
        self.chapters = chapters

class DVDPlayer():
    def __init__(self):
        self.is_on = False
        self.tray_is_open = False
        self.has_dvd = False
        self.play_state = False
        self.current_chapter = 0

    def power_on(self):
        self.is_on = True
        print('Power On')
    
    def power_off(self):
        self.is_on = False
        self.play_state = False
        self.tray_is_open = False
        self.current_chapter = 0
        print('Power Off')

    def toggle_power(self):
        if self.is_on:
            self.is_on = False
            self.play_state = False
            self.tray_is_open = False
            self.current_chapter = 0
            print('Power Off')
        else:
            self.is_on = True
            print('Power On')

    def open_tray(self):
        if self.is_on:
            self.tray_is_open = True
            self.play_state = False
            self.current_chapter = 0
            print('Opened Tray')
        else:
            print('Power is off')

    def close_tray(self):
        if self.is_on:
            self.tray_is_open = False
            print('Closed Tray')
        else:
            print('Power is off')

    def insert_dvd(self,dvd):
        if self.is_on:
            if self.tray_is_open:
                if type(dvd) == type(DVD('',0)):
                    self.has_dvd = True
                    self.dvd = dvd
                    self.current_chapter = 0
                    print('Inserted DVD:',dvd.name)
            else:
                print('Tray is closed')
        else:
            print('Power is off')

    def eject_dvd(self):
        if self.is_on:
            if self.tray_is_open:
                print('Ejected DVD:',self.dvd.name)
                self.has_dvd = False
                self.dvd = None
                self.current_chapter = 0
            else:
                print('Tray is closed')
        else:
            print('Power is off')

    def play_DVD(self):
        if self.is_on:
            if self.tray_is_open == False:
                if self.has_dvd:
                    self.play_state = True
                    print('Now Playing:',self.dvd.name)
                else:
                    print('No DVD')
            else:
                print('Tray is open')
        else:
            print('Power is off')

    def stop_DVD(self):
        if self.is_on:
            if self.tray_is_open == False:
                if self.has_dvd:
                    self.play_state = False
                    print('Stopped Playing:',self.dvd.name)
                else:
                    print('No DVD')
            else:
                print('Tray is open')
        else:
            print('Power is off')

    def skip_forward_chapter(self):
        if self.is_on:
            if self.has_dvd:
                if self.current_chapter < self.dvd.chapters:
                    self.current_chapter += 1
                    print('Skipped to Chapter',self.current_chapter)
                else:
                    print('At Maximum Chapters')
            else:
                print('No DVD')
        else:
            print('Power is off')

    def skip_backward_chapter(self):
        if self.is_on:
            if self.has_dvd:
                if self.current_chapter > 1:
                    self.current_chapter -= 1
                    print('Skipped to Chapter',self.current_chapter)
                else:
                    print('At Minimum Chapters')
            else:
                print('No DVD')
        else:
            print('Power is off')
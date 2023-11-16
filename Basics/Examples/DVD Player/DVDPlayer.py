class DVD():
    def __init__(self,name,chapters):
        self.name = name
        self.chapters = chapters

class DVDPlayer():
    def __init__(self):
        self.is_on,self.play_state,self.tray_is_open,self.has_dvd,self.current_chapter = False,False,False,False,0

    def power_on(self):
        self.is_on = True
        print('Power On')
    
    def power_off(self):
        self.is_on,self.play_state,self.tray_is_open,self.current_chapter = False,False,False,0
        print('Power Off')

    def toggle_power(self):
        if self.is_on:
            self.is_on,self.play_state,self.tray_is_open,self.current_chapter = False,False,False,0
            print('Power Off')
        else:
            self.is_on = True
            print('Power On')

    def open_tray(self):
        if self.is_on:
            self.tray_is_open,self.play_state,self.current_chapter = True,False,0
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
                if not self.has_dvd:
                    if isinstance(dvd,DVD):
                        self.has_dvd,self.dvd,self.current_chapter = True,dvd,0
                        print('Inserted DVD: %s' %(self.dvd.name))
                else:
                    print('DVD Already in Tray')
            else:
                print('Tray is closed')
        else:
            print('Power is off')

    def eject_dvd(self):
        if self.is_on:
            if self.tray_is_open:
                if self.has_dvd:
                    print('Ejected DVD: %s' %(self.dvd.name))
                    self.has_dvd,self.dvd,self.current_chapter = False,None,0
                else:
                    print('No DVD in Tray')
            else:
                print('Tray is closed')
        else:
            print('Power is off')

    def play_DVD(self):
        if self.is_on:
            if self.tray_is_open == False:
                if self.has_dvd:
                    self.play_state = True
                    print('Now Playing: %s' %(self.dvd.name))
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
                    print('Stopped Playing: %s' %(self.dvd.name))
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
                    print('Skipped to Chapter %d' %(self.current_chapter))
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
                    print('Skipped to Chapter %d' %(self.current_chapter))
                else:
                    print('At Minimum Chapters')
            else:
                print('No DVD')
        else:
            print('Power is off')
# Toggle Switch

class ToggleSwitch():
    def __init__(self):
        self.isOn = False

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def toggle(self):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True

    def view_state(self):
        print('Switch Status:',self.isOn)

toggle_switch_1 = ToggleSwitch()
toggle_switch_1.view_state()
toggle_switch_1.toggle()
toggle_switch_1.view_state()
toggle_switch_1.toggle()
toggle_switch_1.view_state()

# Dimmer Switch

class DimmerSwitch():
    def __init__(self):
        self.isOn = False
        self.brightness = 0

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def toggle(self):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True

    def decrease_brightness(self, amount):
        if self.brightness - amount >= 0:
            self.brightness = self.brightness - amount
        else:
            self.brightness = 0

    def increase_brightness(self, amount):
        if self.brightness + amount <= 10:
            self.brightness = self.brightness + amount
        else:
            self.brightness = 10

    def view_state(self):
        print('Switch Status:',self.isOn,'| Switch Brightness:',self.brightness)

dimmer_switch_1 = DimmerSwitch()
dimmer_switch_1.view_state()
dimmer_switch_1.turn_on()
dimmer_switch_1.increase_brightness(2)
dimmer_switch_1.view_state()
dimmer_switch_2 = DimmerSwitch()
dimmer_switch_2.view_state()
dimmer_switch_2.turn_on()
dimmer_switch_2.increase_brightness(3)
dimmer_switch_2.turn_off()
dimmer_switch_2.view_state()
class AirPurifier():
    def __init__(self):
        self.is_on = False
        self.rec_air_is_on = False
        self.level = 1
        self.hep_flt_days = 0
        self.crb_flt_days = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def toggle_power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def turn_on_rec_air(self):
        self.rec_air_is_on = True

    def turn_off_rec_air(self):
        self.rec_air_is_on = False

    def toggle_rec_air(self):
        if self.rec_air_is_on:
            self.rec_air_is_on = False
        else:
            self.rec_air_is_on = True

    def inc_level(self,amount):
        if amount > 0:
            if self.level + amount <= 3:
                self.level = amount
            else:
                self.level = 3
        else:
            print('invalid level')

    def dec_level(self,amount):
        if amount > 0:
            if self.level - amount >= 1:
                self.level = amount
            else:
                self.level = 1
        else:
            print('invalid level')

    def pass_time(self,days):
            self.hep_flt_days += days
            self.crb_flt_days += days

    def check_hep_flt(self):
        if self.hep_flt_days > 10:
            print('HEP A Filter needs to be replaced:',self.hep_flt_days,'days old')
        else:
            print('HEP A Filter is good:',self.hep_flt_days,'days old')

    def replace_hep_flt(self):
        self.hep_flt_days = 0

    def check_crb_flt(self):
        if self.crb_flt_days / 30 > 6:
            print('Carbon Filter needs to be replaced:',round(self.crb_flt_days/30,2),'months old')
        else:
            print('Carbon Filter is good:',round(self.crb_flt_days/30,2),'months old')

    def replace_crb_flt(self):
        self.crb_flt_days = 0

pf_1 = AirPurifier()
pf_1.check_crb_flt()
pf_1.check_hep_flt()
pf_1.pass_time(30)
pf_1.check_crb_flt()
pf_1.check_hep_flt()
pf_1.pass_time(70)
pf_1.check_crb_flt()
pf_1.check_hep_flt()
pf_1.pass_time(200)
pf_1.check_crb_flt()
pf_1.check_hep_flt()
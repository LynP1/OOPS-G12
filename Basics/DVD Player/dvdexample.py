from DVDPlayer import *
Shrek_1 = DVD('Shrek 1',13)
Rush_Hour_2 = DVD('Rush Hour 2',8)
dvd_player_1 = DVDPlayer()

dvd_player_1.power_on()
dvd_player_1.open_tray()
dvd_player_1.insert_dvd(Shrek_1)
dvd_player_1.close_tray()
dvd_player_1.play_DVD()

for x in range(5):
    dvd_player_1.skip_forward_chapter()

dvd_player_1.open_tray()
dvd_player_1.insert_dvd(Rush_Hour_2)
dvd_player_1.close_tray()
dvd_player_1.play_DVD()
for x in range(2):
    dvd_player_1.skip_forward_chapter()

dvd_player_1.stop_DVD()
dvd_player_1.play_DVD()

dvd_player_1.open_tray()
dvd_player_1.eject_dvd()
dvd_player_1.close_tray()
dvd_player_1.play_DVD()

dvd_player_1.toggle_power()
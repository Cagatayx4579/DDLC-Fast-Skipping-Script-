screen debug_jumps():
   if config.developer: 
    key "1" action Jump("ch0_main")
    key "2" action Jump("ch1_main")
    key "3" action Jump("ch2_main")
    key "4" action Jump("ch3_main")
    key "5" action Jump("ch5_main")
    key "6" action Jump("ch10_main")
    key "7" action Jump("ch20_main")
    key "8" action Jump("ch21_main")
    key "9" action Jump("ch22_main")
    key "0" action Jump("ch23_main")
    key "a" action Jump("ch30_main")
    key "b" action Jump("ch40_main")

init python
    config.overlay_screens.append("debug_jumps")

#Copyright (C) Date: 19.06.26 This code is written by AKINCI (ig: @cagatay4579 dc: akinci6607) good luck modders :)
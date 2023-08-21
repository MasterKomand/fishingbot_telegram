#!/usr/bin/bash
pathFile="fishingbot_telegram" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackFish
echo "cd ~/$pathFile/ && python HackFish.py" >  HackFish
chmod +x HackFish
cd ~/
#конец

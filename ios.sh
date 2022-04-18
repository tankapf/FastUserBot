MESAJ="𝙵𝙰𝚂𝚃 𝚄𝚂𝙴𝚁𝙱𝙾𝚃"
MESAJ+="\nTelegram: @FastSupp"
pkg upgrade
clear
echo -e $MESAJ
echo "Python yüklənir..."
pkg install python -y
clear
echo -e $MESAJ
echo "TeleThon yüklənir..."
pip install telethon
echo "Requests/BS4 yüklənir..."
pip install requests
pip install bs4
clear
echo -e $MESAJ
echo "Fayl yazılır..."
curl "https://raw.githubusercontent.com/FastUserBot/FastUserBot/main/fast.py" --output "fast.py"
clear
echo -e $MESAJ
echo "Qurulum Bitdi! İndi String Ala Bilərsiz."
clear
python fast.py

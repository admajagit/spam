import pyautogui
import time

pesan = "Hai!\n"
time.sleep(3)  # Waktu untuk berpindah ke jendela aplikasi

# Mengulangi pengiriman pesan 3 kali
for x in range(3):
    pyautogui.write(pesan)
    pyautogui.press("enter")  # Mengirimkan pesan dengan menekan "Enter"
    time.sleep(2)  # Tunggu 2 detik sebelum mengirim pesan berikutnya

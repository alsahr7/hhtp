
import telebot
import requests
import time
import random

# استبدل بـ API Token الخاص ببوتك
bot = telebot.TeleBot('7647208213:AAFRPnrA_LOtO_7jHfiaMYBNm4hM9pi6rCY')

# وظيفة لقراءة ملف البروكسيهات
def read_proxies(file_path):
    with open(file_path, 'r') as f:
        proxies = f.read().splitlines()
    return proxies

# وظيفة لزيارة موقع باستخدام بروكسي معين
def visit_site(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        print(response)
    except Exception as e:
        print(f"Error: {e}")

# وظيفة رئيسية للبوت
@bot.message_handler(commands=['visit'])
def handle_visit(message):
    url = message.text.split()[1]
    proxies = read_proxies('proxies.txt')  # افترض أن ملف البروكسي يسمى proxies.txt
    while True:
        proxy = random.choice(proxies)
        visit_site(url, proxy)
        time.sleep(300)  # كل 5 دقائق

# تشغيل البوت
bot.polling()
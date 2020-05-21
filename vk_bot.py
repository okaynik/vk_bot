import vk_api
import constants
import time
import random
import otvets

vk = vk_api.VkApi(token=constants.key)

response = vk.method('messages.get', constants.val)


def write_msg(user_id, msg):
    vk.method('messages.send', {'user_id': user_id, 'message': msg})


def send_img(user_id, msg, img):
    vk.method('messages.send', {'user_id': user_id, 'message': msg, 'attachment': img})


while True:
    response = vk.method('messages.get', constants.val)
    if response['items']:
        constants.val['last_message_id'] = response['items'][0]['id']
    for i in response['items']:
        if response['items'][0]['body'].lower() == 'привет' or response['items'][0]['body'].lower() == 'салам' or \
                response['items'][0]['body'].lower() == 'здравствуй':
            rand = random.randint(0, 3)
            write_msg(i['user_id'], otvets.hello[rand])
            write_msg(i['user_id'], '''Напиши "дай пса", если хочешь узнать, какой тебе нужен пёсель
Напиши "Я" и узнай какой пес похож на тебя''')
        elif response['items'][0]['body'].lower() == 'дай пса':
            ch = random.randint(0, 4)
            write_msg(i['user_id'],
                      """Пиши еще, ведь вариантов 🐶 множество

""" + otvets.think[ch] + ' лучше всего вам подойдет')
            choice = random.randint(0, 3)
            print(choice)
            if choice == 0:
                rand = random.randint(1006, 2019)
                send_img(i['user_id'], "Он", 'photo-121355400_45626' + str(rand))
                print(rand)
            elif choice == 1:
                ddd = random.randint(0, 1)
                if ddd == 0:
                    rand = random.randint(300, 364)
                else:
                    rand = random.randint(600, 993)
                send_img(i['user_id'], "Он", 'photo-121355400_456260' + str(rand))
                print(rand)
            elif choice == 2:
                rand = random.randint(1600, 1699)
                send_img(i['user_id'], "Он", 'photo-121355400_45625' + str(rand))
                print(rand)
            elif choice == 3:
                rand = random.randint(6511, 8999)
                send_img(i['user_id'], "Он", 'photo-121355400_45625' + str(rand))
                print(rand)
            time.sleep(1)







        elif response['items'][0]['body'].lower() == 'я':
            ch = random.randint(0, 4)
            write_msg(i['user_id'],
                      """Пиши еще, есть много песелей похожих на тебя

""" + otvets.reflect[ch])
            choice = random.randint(0, 3)
            print(choice)
            if choice == 0:
                rand = random.randint(1006, 2019)
                send_img(i['user_id'], "него", 'photo-121355400_45626' + str(rand))
                print(rand)
            elif choice == 1:
                ddd = random.randint(0, 1)
                if ddd == 0:
                    rand = random.randint(300, 364)
                else:
                    rand = random.randint(800, 993)
                send_img(i['user_id'], "него", 'photo-121355400_456260' + str(rand))
                print(rand)
            elif choice == 2:
                rand = random.randint(1600, 1699)
                send_img(i['user_id'], "него", 'photo-121355400_45625' + str(rand))
                print(rand)
            elif choice == 3:
                rand = random.randint(6511, 8777)
                send_img(i['user_id'], "него", 'photo-121355400_45625' + str(rand))
                print(rand)
            time.sleep(1)
        else:
            write_msg(i['user_id'], '''Напиши "дай пса", если хочешь узнать, какой тебе нужен пёсель
Напиши "Я" и узнай какой пес похож на тебя''')
    time.sleep(1)

import telebot
import random
from telebot import types
client = telebot.TeleBot('my_token')   
@client.message_handler(content_types=['text'])

@client.message_handler(commands=['/hi'])
def hi(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(types.KeyboardButton('/start')) 
    mes = client.send_message(message.from_user.id, "Hi, it's time to play! Choose start", reply_markup = keyboard)
    client.register_next_step_handler(mes, start)

words = [['м','о','р','е'],['д','о','м'],['с','а','д'],['к','о','т'],['п','о','л','е'],['с','т','о','л'],['о','к','н','о'],['к','о','д'],['з','а','м','о','к'],['н','о','с'],['р','е','к','а'],['н','о','ч','ь'],['с','ы','н']]
a = random.choice(words)
b = list(a)

def start(message):
    if message.text == '/start':
        i = 0
        msg = ''
        for b[i] in b:
            b[i] = '_' + ' '  
            msg += b[i]      
            i += 1
        client.send_message(message.from_user.id, msg)
        times = 0
        sent = client.send_message(message.from_user.id, '\nEnter a letter')
        client.register_next_step_handler(sent, user_letter) 

def user_letter(message):
    line = ''
    with open('times.txt') as inf:
        for line in inf:
            line = line.strip()
    times = int(line)
    i = j = k = 0
    letter = message.text       
    if times < 10:  
        if letter.isalpha() and len(letter) == 1:
            letter = letter.lower()   
            cnt = []   
            s = ''     
            if letter in a:
                for k in range(len(a)):
                    if (a[k] == letter) and (k <= len(a) - 1):
                        cnt += str(k)
                    k += 1
                for j in range(len(cnt)):
                    b[int(cnt[j])] = letter
                for j in b:
                    s += j
                client.send_message(message.from_user.id, s)   
                if b != a:
                    client.send_message(message.from_user.id, '\nTries left: ' + str(10 - times))
                    client.send_message(message.from_user.id, '\nEnter a letter - ')
                    client.register_next_step_handler(message, user_letter)
                times += 1
                update_times = open('times.txt', 'w')
                update_times.write(str(times))
                update_times.close()
            else:
                client.send_message(message.from_user.id,'There is no ' + letter)        
                if times < 10:
                    client.send_message(message.from_user.id, '\nTries left: ' + str(10 - times))
                    client.send_message(message.from_user.id, '\nEnter a letter - ')
                    client.register_next_step_handler(message, user_letter)
                times += 1
                update_times = open('times.txt', 'w')
                update_times.write(str(times))
                update_times.close()
            if b == a:
                client.send_message(message.from_user.id,'\nGOOD JOB')
                ouf = open('times.txt', 'w')
                ouf.write('1')
                ouf.close()
                times = 0
                client.send_message(message.from_user.id,'\nText any key to play again!')
            if times == 10 and b != a:
                client.send_message(message.from_user.id,'\nFalure =(\nThe right word was:')
                for j in a:
                    client.send_message(message.from_user.id, j)
                ouf = open('times.txt', 'w')
                ouf.write('1')
                ouf.close()
                times = 0
                client.send_message(message.from_user.id,'\nText any key to play again!')
        else:
            client.send_message(message.from_user.id, 'Incorrect input. Text any key to replay')
              
client.polling(none_stop=True, interval=0)

from transitions.extensions import GraphMachine

from utils import send_text_message, make_message, send_image_url, send_button_message
from life import country, background
from life_data import Country, Background, Event, Ending
from material import life_remake, people_img, end_img
import time


class TocMachine(GraphMachine):
    my_life = []#save the life data
    life_data = []#save the life parameter
    #life data: [country, background, ending]
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def set_country(self, event):
        sender_id = event['sender']['id']
        if event['message'].get("text"):
            text = event['message']['text']
            if text.lower() == 'start':
                return True
            else:
                send_image_url(sender_id, life_remake[0])
                send_text_message(sender_id, "請輸入 start 開始你的人生或說 嗨 或 author")
        else:
            send_text_message(sender_id, "Sorry，只能接收文字，可以說 start 嗨 author")
            return False
         
    def set_background(self, event):
        sender_id = event['sender']['id']
        if event.get('postback'):
            text = event['postback']['payload']
            return text.lower() == 'go'
        else:
            send_text_message(sender_id, "Sorry，請按按鈕")
            return False

    def is_going_to_initial(self, event):
        sender_id = event['sender']['id']
        if event['message'].get("text"):
            text = event["message"]['text']
            if text.lower() == 'remake':
                return True
            else:
                send_text_message(sender_id, '想重刷的話就remake喔')
                return False
        else:
            send_text_message(sender_id, '想重刷的話就remake喔')
            return False

    def set_event(self, event):
        sender_id = event['sender']['id']
        if event.get('postback'):
            text = event['postback']['payload']
            return text.lower() == 'go'
        else:
            send_text_message(sender_id, "Sorry，請按按鈕")
            return False
    
    def set_ending(self, event):
        sender_id = event['sender']['id']
        if event.get('postback'):
            text = event['postback']['payload']
            print('int(text) = ')
            print(int(text))
            if int(text):
                e = int(text)
                #if e < len(Ending[self.life_data[0]][self.life_data[1]]):
                self.life_data.append(e)
                return True
                #else:
                #    return False
            else:
                return False
        else:
            send_text_message(sender_id, "Sorry，請按按鈕")
            return False        
    
    def on_enter_hello(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "你好阿，旅行者")
        self.go_home(event)


    def on_enter_country(self, event):
        #print("your country is set")
        sender_id = event['sender']['id']
        c = country()
        self.my_life.append(c)
        self.life_data.append(Country.index(c))
        buttons = [{
            'type': 'postback',
            'title': 'go',
            'payload': 'go'
        }]
        send_text_message(sender_id, "OH！ 你的首抽為\n" + self.my_life[0] + "人")
        #send_text_message(sender_id, "輸入 go 看看你生在什麼家庭吧")
        send_button_message(sender_id, '按下go，進入下一階段', buttons)

    def on_enter_background(self, event):
        print("your background is set")        
        sender_id = event['sender']['id']
        b = background(self.life_data[0])#random
        self.my_life.append(b)
        self.life_data.append(Background[self.life_data[0]].index(b))
        buttons = [{
            'type': 'postback',
            'title': 'go',
            'payload': 'go'
        }]
        send_text_message(sender_id, "家庭背景：\n" + self.my_life[1])
        send_image_url(sender_id, people_img[Background[self.life_data[0]].index(b)])
        send_button_message(sender_id, '按下go，進入下一階段', buttons)

    def on_enter_event(self, event):
        print("event occur!")
        sender_id = event['sender']['id']
        buttons = []
        if self.life_data[1] == 0:
            buttons = [{
            'type': 'postback',
            'title': '繼承家業',
            'payload': '0'
            },
            {
                'type': 'postback',
                'title': '工作看看',
                'payload': '1'
            },
            {
                'type': 'postback',
                'title': '創業',
                'payload': '2'
            }]
        elif self.life_data[1] == 1:
            buttons = [{
            'type': 'postback',
            'title': '找工作',
            'payload': '0'
            },
            {
                'type': 'postback',
                'title': '啃老',
                'payload': '1'
            },
            {
                'type': 'postback',
                'title': '考公職',
                'payload': '2'
            }]
        elif self.life_data[1] == 2:
            buttons = [{
            'type': 'postback',
            'title': '找工作',
            'payload': '0'
            },
            {
                'type': 'postback',
                'title': '跳陣頭',
                'payload': '1'
            },
            {
                'type': 'postback',
                'title': '簽下去',
                'payload': '2'
            }]    
        #send_text_message(sender_id, Event[self.life_data[0]][self.life_data[1]])
        send_button_message(sender_id, Event[self.life_data[0]][self.life_data[1]], buttons)

    def on_enter_initial(self, event):
        self.life_data.clear()
        self.my_life.clear()
        sender_id = event['sender']['id']
        #send_text_message(sender_id, "輸入 start 刷你的人生首抽喔")

    def on_enter_ending(self, event):
        sender_id = event['sender']['id']
        send_image_url(sender_id, end_img[self.life_data[0]][self.life_data[1]][self.life_data[2]])
        send_text_message(sender_id, Ending[self.life_data[0]][self.life_data[1]][self.life_data[2]]) 
        #send_text_message(sender_id, '想重刷的話就remake喔')

    def on_enter_author_info(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "作者：Wayne\n信箱：ht920055@gmail.com")
        self.go_home(event)
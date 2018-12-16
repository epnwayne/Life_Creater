from transitions.extensions import GraphMachine

from utils import send_text_message, make_message
from life import country, background
from life_data import Country, Background, Event, Work, Ending
import time

class TocMachine(GraphMachine):
    my_life = []#save the life data
    life_data = []#save the life parameter
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    #go to country state
    def set_country(self, event):
        sender_id = event['sender']['id']
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == 'start':
                return True
            else:
                send_text_message(sender_id, "請輸入 start 開始你的人生>_<")
        return False

    #go to background state
    def set_background(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go'
        return False

    def is_going_to_initial(self, event):
        if event.get("message"):
            text = event["message"]['text']
            return text.lower() == 'remake'
        return False

    def set_event(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go'
        return False
    
    def set_ending(self, event):
        if event.get("message"):
            text = event['message']['text']
            if int(text):
                e = int(text)
                if e < len(Ending[self.life_data[0]][self.life_data[1]]):
                    self.life_data.append(e)
                    return True
                else:
                    return False
            else:
                return False

    def on_enter_country(self, event):
        print("your country is set")
        sender_id = event['sender']['id']
        c = country()
        self.my_life.append(c)
        self.life_data.append(Country.index(c))
        #print("country:")
        #print(self.my_life[0])
        send_text_message(sender_id, "OH！ 你的首抽為\n" + self.my_life[0] + "人")
        send_text_message(sender_id, "輸入 go 看看你生在什麼家庭吧")
        

#    def on_exit_state1(self):
#        print('Leaving state1')

    def on_enter_background(self, event):
        print("your background is set")        
        sender_id = event['sender']['id']

        b = background(self.life_data[0])
        #print('life data[0] = \n')
        #print(self.life_data[0])
        self.my_life.append(b)
        self.life_data.append(Background[self.life_data[0]].index(b))
        send_text_message(sender_id, "家庭背景：\n" + self.my_life[1])
        send_text_message(sender_id, "嗯嗯，該說是幸運還是不幸呢\n輸入 go 進入下一階段")

#    def on_exit_state2(self):
#        print('Leaving state2')

    def on_enter_event(self, event):
        print("event occur!")
        sender_id = event['sender']['id']
        #print('life data[1] = \n')
        #print(self.life_data[1])
        send_text_message(sender_id, Event[self.life_data[0]][self.life_data[1]])
        

    def on_enter_initial(self, event):
        print("I'm going initial")
        self.life_data.clear()
        self.my_life.clear()
        sender_id = event['sender']['id']
        send_text_message(sender_id, "想重刷是吧？那就輸入 start 重刷你的人生首抽")

    def on_enter_ending(self, event):
        print('is ending!') 
        sender_id = event['sender']['id']
        send_text_message(sender_id, Ending[self.life_data[0]][self.life_data[1]][self.life_data[2]]) 
        send_text_message(sender_id, '想重刷的話就remake喔')      

#    def on_exit_user(self):
#        print('Leaving user')

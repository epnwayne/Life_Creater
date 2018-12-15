from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
#check if it is going to state1

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def is_going_to_user(self, event):
        if event.get("message"):
            text = event["message"]['text']
            return text.lower() == 'go home'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False
    
    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        #self.go_back()

#    def on_exit_state1(self):
#        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        #self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm going state3")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm going state3^__^")
        
    def on_enter_user(self, event):
        print("I'm going home")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm going home,FUCK YOU")

#    def on_exit_user(self):
#        print('Leaving user')

import os
from bottle import route, run, request, abort, static_file
from fsm import TocMachine

PORT = os.environ['PORT']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

machine = TocMachine(
    states=[
        'initial',
        'country',
        'background',
        'event',
        'ending',
        'hello',
        'author_info'
    ],
    transitions=[
        {
            'trigger': 'author',
            'source': 'initial',
            'dest': 'author_info'
        }
        {
            'trigger': 'hi',
            'source': 'initial',
            'dest': 'hello',
        },
        {
            'trigger': 'go_home',
            'source': ['hello', 'author_info'],
            'dest': 'initial'
        },
        {
            'trigger': 'first',
            'source': 'initial',
            'dest': 'country',
            'conditions': 'set_country'
        },
        {
            'trigger': 'second',
            'source': 'country',
            'dest': 'background',
            'conditions': 'set_background'
        },
        {
            'trigger': 'remake',
            'source': ['ending', 'initial'],
            'dest': 'initial',
            'conditions': 'is_going_to_initial'
        },
        {
            'trigger': 'third',
            'source': 'background',
            'dest': 'event',
            'conditions': 'set_event'
        },
        {
            'trigger':'end',
            'source':'event',
            'dest':'ending',
            'conditions':'set_ending'
        }
    ],
    initial='initial',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        print('current state:')
        print(machine.state)
        if event.get('message') and event['message'].get('text'):
            text = event['message']['text']
            if text == '嗨' or text == 'hi' or text == 'hello':
                machine.hi(event)
        if machine.state == 'initial':
            machine.first(event)
        elif machine.state == 'country':
            machine.second(event)
        elif machine.state == 'background':
            machine.third(event)
        elif machine.state == 'event':
            machine.end(event)
        elif machine.state == 'ending':
            machine.remake(event)      
        return 'OK'

#        if text == "go to state1":
#            machine.state1(event)
#        if text == "go to state2":
#            machine.state2(event)
#        if text == "go to user":
#            machine.user(event)    


        


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

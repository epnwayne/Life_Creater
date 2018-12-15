from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': ['state1', 'state2', 'state3'],
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': ['state1', 'state2'],
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        }
    ],
    initial='user',
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

@route("/", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
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
    run(host="localhost", port=5000, debug=True, reloader=True)

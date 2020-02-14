from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

base_intents = ['faturamento_img', 'faturamento_txt', 'faturamento_audio', 'faturamento']

api_key = '<Api key>'
authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2020-02-12',
    authenticator=authenticator
)
service_url = '<service url>'

assistant.set_service_url(service_url)

# assistant.set_disable_ssl_verification(True)

assistant_id = '<assistant_id>'
session = assistant.create_session(assistant_id).get_result()
session_id = session['session_id']

while(1):
    print('eu: ', end='')
    user_input = input()
    message = assistant.message(
        assistant_id,
        session_id,
        input={'text': user_input},
        context={
            'metadata': {
                'deployment': 'myDeployment'
            }
        }).get_result()
    
    print(json.dumps(message, indent=2))
    response = message['output']['generic']
    for r in response:
        if r['response_type']=='text':
            response_text = r['text']
        
    print('clara tupiniquim: ', response_text)
    
    if(message['output']['intents']!=[]):
        intent = message['output']['intents'][0]['intent']
        if(intent in base_intents):
            print('ok, redirecionando para fluxo de {}'.format(intent))
            break



quit()
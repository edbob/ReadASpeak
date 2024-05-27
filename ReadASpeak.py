import eel
from telethon import Button, TelegramClient, events, errors
from gtts import gTTS
import os, time
import emoji
import config

client = TelegramClient(config.User['name_client'], config.User['api_id'], config.User['api_hash'])


@eel.expose
@client.on(events.NewMessage(chats=config.User['HasID']))
async def my_event_handler(event):
   
#Text on Сleaning
    def TextСleaning(inputString):
        return emoji.replace_emoji(inputString,'')

    try:
    #converted text in mp3 file
        tts = gTTS(text=TextСleaning(event.text), lang='uk', slow=False) # type: ignore
                
    # Saving the converted audio in a mp3 file named
        tts.save("random.mp3")
                
    # Playing the converted file
        for _ in range(2):
            os.system("start random.mp3")
            
    except:
        pass
            
    #Send mp3 in telegram
        #await client.send_file(conf.User['ChatSend'], 'random.mp3', voice_note=True)
    #print text in terminal
    
    print(f'User:({event.sender.first_name}) in {event.chat.title}, text: "{TextСleaning(event.text)}"') # type: ignore
    
try:
    #Starting
    if __name__ == '__main__':
        print('Starting bot...')

        #Starting as a user account.  
        client.start()

        #Polls the bot
        print('Polling...')

        #Runs the event loop until the library is disconnected.
        client.run_until_disconnected()

        #If you klick "ctr C"
        print('disconnected!')
        
except OSError as error:
    print("Результат ошибки: ", error)
    
eel.init('./web')
eel.start('main.html', mode='chrome-app', port=3333, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'], size= (200, 100), position= (300, 50))
#eel.start('main.html', size=(400, 400) , position=(500, 500), port=8888)  

from discord import Client, Intents
import responses
from api_key import key

def run_bot(token: str):
    
    # Basic bot setup
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)

    knowledge: dict = responses.load_knowledge('29_discord_bot_mine/knowledge.json')

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content:
            print(f'({message.channel}) {message.author}: {message.content}')
            response: str = responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)

        else:
            print('!!! Carepinga usa las palabras correctas !!!!')

    client.run(token=token)

if __name__ == "__main__":
    run_bot(token=key)

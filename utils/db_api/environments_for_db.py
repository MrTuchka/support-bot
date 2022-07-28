from utils.db_api.dbconfig import get

db = dict()

async def get_db():
    start_command = await get('SidisTestsBot', 'setup', 'start_command')
    db['start_command'] = start_command

    send_command = await get('SidisTestsBot', 'setup', 'send_command')
    db['send_command'] = send_command

    greetings_text = await get('SidisTestsBot', 'setup', 'greetings_text')
    db['greetings_text'] = greetings_text

    stop_text = await get('SidisTestsBot', 'setup', 'stop_text')
    db['stop_text'] = stop_text

    start_chat_text = await get('SidisTestsBot', 'setup', 'start_chat_text')
    db['stop_text'] = start_chat_text




#get all the good stuff going

def getMessage():
    messages = queue_service.get_messages('acceldata')
    for message in messages:
        return message.message_text
        queue_service.delete_message('acceldata', message.message_id, message.pop_receipt)
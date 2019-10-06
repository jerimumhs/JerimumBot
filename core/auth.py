
def adm_verify(update):
    return update.message.chat.get_member(update.message.from_user.id)\
               .status in ('creator', 'administrator')

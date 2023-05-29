import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

#api-key = vk1.a.t9U8dwwX7L2XFyqrz6Iwq8bRIW8BQsOodLpd5DGVqDmrEpLylPEGfdFp8VGdjYjw_XdSkjTo1QdIg3fG6kMTaWo7aQMjXN9WOCoEitzvlm_pL2pJ4fji81xUvg6Q_dsIO8CObCySsBmUKoOF9_h9u_ULUFQHdYEbboV1dyL9TwVzy296wNfUEmRd3VcNej5CyC41Hye6HFQ1TNFk1eMe2Q


#Привет [Имя пользователя]
def main():

    vk_session = vk_api.VkApi(token = 'vk1.a.t9U8dwwX7L2XFyqrz6Iwq8bRIW8BQsOodLpd5DGVqDmrEpLylPEGfdFp8VGdjYjw_XdSkjTo1QdIg3fG6kMTaWo7aQMjXN9WOCoEitzvlm_pL2pJ4fji81xUvg6Q_dsIO8CObCySsBmUKoOF9_h9u_ULUFQHdYEbboV1dyL9TwVzy296wNfUEmRd3VcNej5CyC41Hye6HFQ1TNFk1eMe2Q')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text:
            print('New from {}, text = {}'.format(event.user_id, event.text))

            vk.messages.send(
                user_id = event.user_id,
                random_id = get_random_id(),
                message = 'Привет, ' + \
                    vk.users.get(user_id = event.user_id)[0]['first_name']
            )
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('New from {}, text = {}'.format(event.user_id, event.text))

if __name__ ==  '__main__':
    main()
import vk
import time

#авторизация
session = vk.Session(access_token='55d012fa6b25d3177a7860aa8b6468c2dda6f3978c8c4e2e08385aeaffe2e37e0bb4fe164fdc90750eabf')
api = vk.API(session)

post = api.wall.get(owner_id=-93077522, count=1, offset=10)
print(post)
#ссылка на фото из поста
photo = post[1]['attachment']['photo']['src_big']
#id группы
owner = post[1]['media']['owner_id']
#id фото
item = post[1]['media']['item_id']
#предыдущее сообщение
prev_m = api.messages.get(out=1, count=3, offset=0)
for i in range (0, 21):
    api.messages.send(user_id=155533300, attachment='photo'+str(owner)+'_'+str(item))
    time.sleep(1)

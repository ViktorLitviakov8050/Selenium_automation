# def func(s1, s2):
#     return s1, s2
#
# s1 = 'Python'
# s2 = 'Learning'
# result = func(s1, s2)[0]
# print(result.replace('P', 'T'))


import aiocron
import asyncio
@aiocron.crontab('*/1 * * * *')
async def hi():
    print('Hello!')
asyncio.get_event_loop().run_forever()
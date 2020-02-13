import redis


try:
    conn=redis.StrictRedis(
    host='localhost',
    port=6379,
    password='',
    ssl=True,
    decode_responses=True
)   
    print (conn)
    print ('Connected!')
    print ('before set!')
    conn.set('nnn', 'yguyfgyuvf')
    print ('after set!')
    msg = conn.get('nnn')

    print(msg)
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')
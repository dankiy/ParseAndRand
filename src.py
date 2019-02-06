import requests
import random

a_token = "" #vk token
owner_id = "-151755775"
query = "как"
v = "5.92"

r1 = requests.get("https://api.vk.com/method/wall.search?owner_id="+owner_id+
                  "&query="+query+"&count=1&access_token="+a_token+"&v="+v)
poll = r1.json().get("response").get("items")[0].get("attachments")[0].get("poll")
poll_id = str(poll.get("id"))
answer0_id = str(poll.get("answers")[0].get("id"))
answer1_id = str(poll.get("answers")[1].get("id"))
answer2_id = str(poll.get("answers")[2].get("id"))

r2 = requests.get("https://api.vk.com/method/polls.getVoters?poll_id="+poll_id+
                  "&answer_ids="+answer0_id+","+answer1_id+","+answer2_id+"&access_token="+a_token+"&v="+v)
user_ids1 = r2.json().get("response")[0].get("users").get("items")
user_ids2 = r2.json().get("response")[1].get("users").get("items")
user_ids3 = r2.json().get("response")[2].get("users").get("items")

get1 = requests.get("https://api.vk.com/method/users.get?user_ids="+''.join(str(id)+',' for id in user_ids1)
                    +"&access_token="+a_token+"&v="+v).json().get("response")
get2 = requests.get("https://api.vk.com/method/users.get?user_ids="+''.join(str(id)+',' for id in user_ids2)
                    +"&access_token="+a_token+"&v="+v).json().get("response")
get3 = requests.get("https://api.vk.com/method/users.get?user_ids="+''.join(str(id)+',' for id in user_ids3)
                    +"&access_token="+a_token+"&v="+v).json().get("response")
q1 = [str(get1[i].get("first_name")+" "+get1[i].get("last_name")) for i in range(0, len(get1))]
q2 = [str(get2[i].get("first_name")+" "+get2[i].get("last_name")) for i in range(0, len(get2))]
q3 = [str(get3[i].get("first_name")+" "+get3[i].get("last_name")) for i in range(0, len(get3))]

iter = 1
n1 = len(q1)
for i in range(5):
    if n1 == 0:
        break
    r = random.randint(0, n1-1)
    print(str(iter) + " " + str(q1.pop(r)))
    n1 -= 1
    iter += 1
q2.extend(q1)
n2 = len(q2)
for i in range(5):
    if n2 == 0:
        break
    r = random.randint(0, n2-1)
    print(str(iter) + " " + str(q2.pop(r)))
    n2 -= 1
    iter += 1
q3.extend(q2)
n3 = len(q3)
while n3 != 0:
    r = random.randint(0, n3-1)
    print(str(iter) + " " + str(q3.pop(r)))
    n3 -= 1
    iter += 1
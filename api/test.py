import requests 

base="http://127.0.0.1:5000/"
data=[
    {"likes":10, "name":"sid1","views":20},
    {"likes":20, "name":"sid2","views":2000},
    {"likes":30, "name":"sid3","views":3000},
    {"likes":40, "name":"sid4","views":4000},
    {"likes":50, "name":"sid1","views":5000},
    ]
print("_____________put_____________")
for i in range(len(data)):
    response= requests.put(base + "/video/"+str(i), data[i])
    print(response.json())
print("_____________Get_____________")
for i in range(len(data)):
    response=requests.get(base + "/video/"+str(i))
    print(response.json())
# print("_____________deleat_____________")
# response=requests.delete(base + "/video/0")
# print(response)
# i=input()
# response=requests.put(base + "/video/1" , {"likes":10, "name":"sid","views":1000} )

# response=requests.get(base + "/video/2")
# print(response.json())


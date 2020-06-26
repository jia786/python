import requests
url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'
x=requests.post(url,json={"qconfig":"<<config parameters>>","userID":525067,"githubLink":"https://github.com/jia786/python"})
print(x.text)

#_*_ coding:utf-8 _*_
from flask import Flask
from gitlabApi import GitlabApi

#############
## gunicorn -w 4 -b 127.0.0.1:5000 -D main:app
############

app = Flask(__name__)


@app.route('/spendTimeDatas',methods=['GET'])
def getDatas():
    api = GitlabApi('ycyin')
    return api.getDatasWithList() 

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
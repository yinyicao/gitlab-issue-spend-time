#_*_ coding:utf-8 _*_
from flask import Flask
from gitlabApi import GitlabApi

#############
## gunicorn -w 4 -b 127.0.0.1:5000 -D main:app
############

app = Flask(__name__)


@app.route('/projects',methods=['GET'])
def getProjects():
    api = GitlabApi('ycyin')
    return api.getProjects()

@app.route('/issues',methods=['GET'])
def getIssues():
    api = GitlabApi('ycyin')
    return api.getIssues()


@app.route('/issueNotesHasTime',methods=['GET'])
def getIssueNotesHasTime():
    api = GitlabApi('ycyin')
    return api.getIssueNotesHasTime()  


@app.route('/projectIds',methods=['GET'])
def getProjectIds():
    api = GitlabApi('ycyin')
    return api.getProjectIds()

@app.route('/todayIssues',methods=['GET'])
def getTodayIssues():
    api = GitlabApi('ycyin')
    return api.getIssueWithUpdateTodayAndOpend()      


@app.route('/issueNotes',methods=['GET'])
def getIssueNotes():
    api = GitlabApi('ycyin')
    return api.getIssueNotes()  


@app.route('/getIssueAddTime',methods=['GET'])
def getIssueAddTime():
    api = GitlabApi('ycyin')
    return api.getIssueAddTime() 

@app.route('/getDatas',methods=['GET'])
def getDatas():
    api = GitlabApi('ycyin')
    return api.getDatas() 

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
#_*_ coding:utf-8 _*_
import requests,json
import time,datetime
import re

class GitlabApi:
    project_url = 'https://git.cae.com/api/v4/projects'
    headers = {'PRIVATE-TOKEN':''}
    def __init__(self,name):
        self.name = name

    def getProjects(self):
        r = requests.get(self.project_url,headers=self.headers,verify=False)
        return r.content

    def getProjectIds(self):
        projects  = json.loads(self.getProjects())
        ids = []
        for project in projects:
            ids.append(project['id'])   
        return json.dumps(ids)
    
    # 获取近15天的Issue
    def getIssueWithUpdateTodayAndOpend(self):
        ids = json.loads(self.getProjectIds())
        issues = []
        for _id in ids:
          r = requests.get(self.project_url+"/"+str(_id)+"/issues",headers=self.headers,verify=False)
          _issues = json.loads(r.content)
          for _issue in _issues:
            # now_date = datetime.datetime.now().strftime("%Y-%m-%d")
            # now_date = datetime.datetime.strptime('2021-1-13',"%Y-%m-%d").strftime("%Y-%m-%d")
            # 当前日期减少15天
            fifteenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=15)).strftime("%Y-%m-%d")
            print(fifteenDayAgo)
            created_at_date = datetime.datetime.strptime(_issue['created_at'],"%Y-%m-%dT%H:%M:%S.%f+08:00").strftime("%Y-%m-%d")
            # 转为时间戳
            fifteenDayAgo2 = time.mktime(time.strptime(fifteenDayAgo,"%Y-%m-%d"))
            created_at_date2 = time.mktime(time.strptime(created_at_date,"%Y-%m-%d"))
            # if now_date == created_at_date:
            if created_at_date2 >= fifteenDayAgo2:
                issues.append(_issue)
        return json.dumps(issues)

    # 获取包含近15天的记录信息的Issue Notes
    def getIssueNotes(self):
        issues = json.loads(self.getIssueWithUpdateTodayAndOpend())
        allNotes = []
        for _issue in issues:
            r = requests.get(self.project_url+"/"+str(_issue['project_id'])+"/issues/"+str(_issue['iid'])+"/notes",headers=self.headers,verify=False)
            _notes = json.loads(r.content)
            for _note in _notes:
                # now_date = datetime.datetime.now().strftime("%Y-%m-%d")
                # now_date = datetime.datetime.strptime('2021-1-13',"%Y-%m-%d").strftime("%Y-%m-%d")
                # 当前日期减少15天
                fifteenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=15)).strftime("%Y-%m-%d")
                created_at_date = datetime.datetime.strptime(_issue['created_at'],"%Y-%m-%dT%H:%M:%S.%f+08:00").strftime("%Y-%m-%d")
                # 转为时间戳
                fifteenDayAgo2 = time.mktime(time.strptime(fifteenDayAgo,"%Y-%m-%d"))
                created_at_date2 = time.mktime(time.strptime(created_at_date,"%Y-%m-%d"))
                # if now_date == created_at_date:
                if created_at_date2 >= fifteenDayAgo2:
                        allNotes.append(_note)
        return json.dumps(allNotes)

    # 获取包含报工信息的Issue Notes
    def getIssueAddTime(self):
        _notes = json.loads(self.getIssueNotes())
        allNotes = []
        for _note in _notes:
            rr=re.findall(r"[subtracted|added](.+?)of time spent at", _note['body'])
            if len(rr) != 0:
                allNotes.append(_note)
        return json.dumps(allNotes)

    # 根据Issue Notes统计数据
    def getDatas(self):
        _notes = json.loads(self.getIssueAddTime())
        datas = {}
        for _note in _notes:
            data = []
            person = {}
            addhours = re.findall(r"added(.+?)of time spent at", _note['body'])
            subhours = re.findall(r"subtracted(.+?)of time spent at", _note['body'])
            date = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", _note['body'])
            # /spend 7h 
            if len(addhours) != 0:
                strTime = re.findall(r"(.+?)h", addhours[0].strip())[0]
                ## 获取已经存在的日期数据
                ndata = datas.get(date[0],-1)
                if(ndata != -1):
                    ## 存在 取对应人的数据
                    flag = False
                    for p in ndata:
                        if p['name'] == _note['author']['name']:
                            flag = True
                            p['time'] = p['time'] + int(strTime)
                    if flag == False:
                        person['name'] = _note['author']['name']
                        person['avatar_url'] = _note['author']['avatar_url']
                        person['time'] = int(strTime)
                        ndata.append(person)
                else:
                    person['name'] = _note['author']['name']
                    person['avatar_url'] = _note['author']['avatar_url']
                    person['time'] = int(strTime)
                    data.append(person)
                    datas[date[0]] = data
            # /spend -7h        
            if len(subhours) != 0:
                strTime = re.findall(r"(.+?)h", subhours[0].strip())[0]
                ## 获取已经存在的日期数据
                ndata = datas.get(date[0],-1)
                if(ndata != -1):
                    ## 存在 取对应人的数据
                    ## flag标识是否有对应人的数据
                    flag = False
                    for p in ndata:
                        if p['name'] == _note['author']['name']:
                            flag = True
                            p['time'] = p['time'] - int(strTime)
                    if flag == False:
                        person['name'] = _note['author']['name']
                        person['avatar_url'] = _note['author']['avatar_url']
                        person['time'] = 0 - int(strTime)
                        ndata.append(person) 
                else:
                    person['name'] = _note['author']['name']
                    person['avatar_url'] = _note['author']['avatar_url']
                    person['time'] = 0 - int(strTime)
                    data.append(person)
                    datas[date[0]] = data   
        # 排序
        result = {}
        for i in sorted(datas):
            result[i] = datas[i] 

        return json.dumps(result)

if __name__ == "__main__":
    pass
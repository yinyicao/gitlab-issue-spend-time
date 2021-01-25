#_*_ coding:utf-8 _*_
import re, ujson,gitlab
from Utils import dateTimeUtil
#https://python-gitlab.readthedocs.io/en/stable/

class GitlabApi:
    gitlab_url = 'https://xxx.com'
    gitlab_private_token = ''
    gl = gitlab.Gitlab(url=gitlab_url, private_token = gitlab_private_token,ssl_verify=False)
    def __init__(self,name):
        self.name = name


    def getIssuesUpdatedDaysAgo(self,days=0):
        ## '2020-12-15T08:00:00Z'
        updated_after_time = dateTimeUtil.getIsoLocalDateTimeAgo(days)
        return self.gl.issues.list(updated_after=updated_after_time,scope='all',all=True)    

    def getIssueNotesSevenDaysAgo(self):
        allNotes = []
        for issue in self.getIssuesUpdatedDaysAgo(15):
            project_issue = self.gl.projects.get(issue.project_id, lazy=True).issues.get(issue.iid, lazy=True)
            i_notes = project_issue.notes.list()
            for i_note in i_notes:
                rr=re.findall(r"[subtracted|added](.+?)of time spent at", i_note.body)
                # 取包含subtracted|added信息的issue note
                if len(rr) != 0:
                    # 将issue note的updated_at时间转为时间戳
                    i_note_date_timestamp = dateTimeUtil.toTimeStampWithFormatFromisoformat(i_note.updated_at)
                    # 将当前时间前x天的日期时间转换为时间戳
                    seven_days_ago_date_timestamp = dateTimeUtil.toTimeStampWithFormatFromisoformat(dateTimeUtil.getIsoLocalDateTimeAgo(7))
                    # 取近x天的issue note
                    if i_note_date_timestamp >= seven_days_ago_date_timestamp:
                        allNotes.append(i_note)
        return allNotes

 
    def getDatasWithDict(self):
        """
            根据Issue Notes统计数据，以Dict返回
            数据格式：
                {
                "2021-01-15": [
                    {
                    "name": "张三",
                    "avatar_url": "https://xxx.x/email/zhangsan/avatar.png",
                    "time": 7
                    },
                    {
                    "name": "李四",
                    "avatar_url": "https://xxx.x/email/lisi/avatar.png",
                    "time": 7
                    },
                    // ...
                ],
                "2021-01-18": [

                ],
                // ...
                }
        """
        _notes = self.getIssueNotesSevenDaysAgo()
        datas = {}
        for _note in _notes:
            data = []
            person = {}
            addhours = re.findall(r"added(.+?)of time spent at", _note.body)
            subhours = re.findall(r"subtracted(.+?)of time spent at", _note.body)
            date = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", _note.body)
            # /spend 7h 
            if len(addhours) != 0:
                strTimeArr = re.findall(r"(.+?)h", addhours[0].strip())
                intTime = 0
                ## 确定只有一个值
                if len(strTimeArr) != 0:
                    intTime = int(strTimeArr[0])
                ## 获取已经存在的日期数据
                ndata = datas.get(date[0],-1)
                if(ndata != -1):
                    ## 存在 取对应人的数据
                    flag = False
                    for p in ndata:
                        if p['name'] == _note.author['name']:
                            flag = True
                            p['time'] = p['time'] + intTime
                    if flag == False:
                        person['name'] = _note.author['name']
                        person['avatar_url'] = _note.author['avatar_url']
                        person['time'] = intTime
                        ndata.append(person)
                else:
                    person['name'] = _note.author['name']
                    person['avatar_url'] = _note.author['avatar_url']
                    person['time'] = intTime
                    data.append(person)
                    datas[date[0]] = data
            # /spend -7h        
            if len(subhours) != 0:
                strTimeArr = re.findall(r"(.+?)h", subhours[0].strip())
                intTime = 0
                ## 确定只有一个值
                if len(strTimeArr) != 0:
                    intTime = int(strTimeArr[0])
                ## 获取已经存在的日期数据
                ndata = datas.get(date[0],-1)
                if(ndata != -1):
                    ## 存在 取对应人的数据
                    ## flag标识是否有对应人的数据
                    flag = False
                    for p in ndata:
                        if p['name'] == _note.author['name']:
                            flag = True
                            p['time'] = p['time'] - intTime
                    if flag == False:
                        person['name'] = _note.author['name']
                        person['avatar_url'] = _note.author['avatar_url']
                        person['time'] = 0 - intTime
                        ndata.append(person) 
                else:
                    person['name'] = _note.author['name']
                    person['avatar_url'] = _note.author['avatar_url']
                    person['time'] = 0 - intTime
                    data.append(person)
                    datas[date[0]] = data   
        # 排序
        result = {}
        for i in sorted(datas):
            result[i] = datas[i] 

        return ujson.dumps(result)

    
    def handleSpendTime(self,_person,_date,_time):
        """
            处理数据
        """
        # 从已知的字典中获取数据，获取到累加，未获取到新增
        ndataTime = _person.get(_date,-1)
        if(ndataTime != -1):
            _person[_date] = ndataTime + _time
        else:
            _person[_date] = _time


    def getDatasWithList(self):
        """
        根据Issue Notes统计数据,以List返回
        数据格式：
            [
                {
                    "name": "张三",
                    "avatar_url": "https://xxx.x/email/zhangsan/avatar.png",
                    "2021-01-21": 7,
                    "2021-01-20": 7,
                    // ...
                },
                {
                    "name": "尹以操",
                    "avatar_url": "https://xxx.x/email/lisi/avatar.png",
                    "2021-01-21": 7,
                    // ...
                },
                // ...
                ]
        """
        _notes = self.getIssueNotesSevenDaysAgo()
        datas = {}
        for _note in _notes:
            # 获取一个存在的以姓名为key的value 或者创建一个新的
            person = datas.get(_note.author['name'],{'name':_note.author['name'],'avatar_url':_note.author['avatar_url']})
            addhours = re.findall(r"added(.+?)of time spent at", _note.body)
            subhours = re.findall(r"subtracted(.+?)of time spent at", _note.body)
            date = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", _note.body)
            # /spend 7h 
            if len(addhours) != 0:
                strTimeArr = re.findall(r"(.+?)h", addhours[0].strip())
                ## 确定只有一个值
                if len(strTimeArr) != 0:
                    intTime = int(strTimeArr[0])
                    self.handleSpendTime(person,date[0],intTime)
            # /spend -7h    
            if len(subhours) != 0:
                strTimeArr = re.findall(r"(.+?)h", subhours[0].strip())
                ## 确定只有一个值
                if len(strTimeArr) != 0:
                    intTime = 0 - int(strTimeArr[0])  
                    self.handleSpendTime(person,date[0],intTime)

            # append to datas
            datas[person['name']] = person
        # the values() menthod in Python 3 no longer returns an array, instead we have a dict_values wrapper around the data.
        # https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict    
        result = list(datas.values()) 

        return ujson.dumps(result)

if __name__ == "__main__":
    pass
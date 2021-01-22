import time,datetime,ujson

class dateTimeUtil:

    @staticmethod
    def getLocalDateTime():
        """
            获取本地当前时间
        """
        return datetime.datetime.now()

    @staticmethod
    def getLocalDataTimeWithFormat(format='%Y-%m-%dT%H:%M:%S%Z'):
        """
            获取本地当前时间(带格式)
        """
        return dateTimeUtil.getLocalDateTime().strftime(format) 
    
    @staticmethod
    def toTimeStampWithFormatFromisoformat(isodateTimeStr):
        """
            ISO格式(2021-01-21T16:43:42.988+08:00)的日期时间字符串转换为时间戳
        """
        return datetime.datetime.fromisoformat(isodateTimeStr).timestamp()      

    @staticmethod
    def getLDTWithoutMS():
        """
            获取本地当前时间(无毫秒) getLocalDateTimeWithoutMicrosecond
        """
        return dateTimeUtil.getLocalDateTime().replace(microsecond=0)    
    
    @staticmethod
    def getIsoLDTWithoutMS():
        """
            获取当前本地ISO 8601格式的时间(无毫秒) getIsoLocalDateTime
        :return:
        """
        return dateTimeUtil.getLDTWithoutMS().isoformat()

    @staticmethod
    def getIsoLocalDateTimeAgo(daysForAgo=0):
        """
            获取指定天数前本地ISO 8601格式的时间(无毫秒)
        :param daysForAgo: 天数
        :return:
        """
        return (dateTimeUtil.getLocalDateTime()- datetime.timedelta(days=daysForAgo)).replace(microsecond=0).isoformat()

if __name__ == '__main__':
    print(dateTimeUtil.getIsoLDTWithoutMS())
    print(dateTimeUtil.getLocalDataTimeWithFormat('%Y-%m-%d'))
    print(dateTimeUtil.getIsoLocalDateTimeAgo(1))
    print(dateTimeUtil.getIsoLocalDateTimeAgo())        
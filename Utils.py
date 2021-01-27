import time,datetime,ujson

class dateTimeUtil:

    @staticmethod
    def getLocalDateTime():
        """
            获取本地当前时间
            :return: example '2021-01-27 09:57:56.727491'
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
            getLocalDateTimeWithoutMicrosecond
            获取本地当前时间(无毫秒)
            :return: example '2021-01-27 09:56:44' 
        """
        return dateTimeUtil.getLocalDateTime().replace(microsecond=0)    
    
    @staticmethod
    def getIsoLDTWithoutMS():
        """
            getIsoLocalDateTime
            获取当前本地ISO 8601格式的时间(无毫秒) 
        :return: example '2021-01-27T09:54:55' 
        """
        return dateTimeUtil.getLDTWithoutMS().isoformat()

    @staticmethod
    def getIsoLocalDateTimeAgo(daysForAgo=0):
        """
            获取指定天数前本地ISO 8601格式的时间(无毫秒)
        :param daysForAgo: 天数
        :return: example '2021-01-20T09:48:32' 
        """
        return (dateTimeUtil.getLocalDateTime()- datetime.timedelta(days=daysForAgo)).replace(microsecond=0).isoformat()

    @staticmethod
    def getIsoLocalDateAgo(daysForAgo=0):
        """
            获取指定天数前本地ISO 8601格式的日期(不包含时间)
        :param daysForAgo: 天数
        :return: example '2021-01-20'
        """
        return  (dateTimeUtil.getLocalDateTime()- datetime.timedelta(days=daysForAgo)).replace(microsecond=0).date().isoformat()   

if __name__ == '__main__':
    print(dateTimeUtil.getLocalDateTime())
    print(dateTimeUtil.getLDTWithoutMS())
    print(dateTimeUtil.getIsoLDTWithoutMS())
    print(dateTimeUtil.getLocalDataTimeWithFormat('%Y-%m-%d'))
    print(dateTimeUtil.getIsoLocalDateTimeAgo(1))
    print(dateTimeUtil.getIsoLocalDateTimeAgo())        
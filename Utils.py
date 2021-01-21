import time,datetime


class dateTimeUtil:
    
    @staticmethod
    def getIsoLocalDateTimeNow():
        """
            获取当前本地ISO 8601格式的时间
        :return:
        """
        return datetime.datetime.now().isoformat()

    @staticmethod
    def getIsoLocalDateTimeAgo(daysForAgo):
        """
            获取指定天数前本地ISO 8601格式的时间
        :param daysForAgo: 天数
        :return:
        """
        return (datetime.datetime.now() - datetime.timedelta(days=daysForAgo)).isoformat()
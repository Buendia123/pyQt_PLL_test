class SZDbSetting:
    server = '172.16.26.26'
    database = 'HSATE_Eng'
    logtable = 'UTPTestLog'
    resulttable = 'UTPTest'
    user = 'acccable'
    password = 'K6$7uAuegP'


class SZMesSetting:
    host_checksn = r'http://172.16.26.86/v5mesapi//openapi/mes/tracking/check'
    host_postresult = r'http://172.16.26.86/v5mesapi//openapi/mes/tracking'
    operationId = r'3fa85f64-5717-4562-b3fc-2c963f66afa6'
    userid = 'V005885'


class DbProvider:
    Db = SZDbSetting()
    Mes = SZMesSetting()

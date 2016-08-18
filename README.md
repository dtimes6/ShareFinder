# ShareFinder
利用Tushare选股

以下是初步接触Tushare 20分钟学到的使用方法

    import tushare as ts              #加载tushare
    data = ts.get_hist_data('000002') #获取万科A的历史数据
    dat15 = data.head(15)             #获取最近15个交易日的数据
    p_change15 = dat15['p_change']    #获取最近15个交易日的‘pchange’，也就是涨跌幅度数据
    p_change15.size                   #数据表长度，这里是15 
    dat15.keys()                      #获取表头

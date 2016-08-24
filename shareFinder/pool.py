import datetime;
import tushare as ts;

class StockList:
    def __init__(self, l):
        self.__list = l;

    def filter(self, strategy):
        return StockList(filter(strategy, self.__list));


def get_full_stock_list():
    info = ts.get_stock_basics();
    return StockList(sorted(info.index));


def latest_drop_in_days_greater(days, percentage):
    now = datetime.datetime.now();
    delta = datetime.timedelta(days=days);
    before = now - delta;
    time_before = before.strftime("%Y-%m-%d");
    def func(code):
        d = ts.get_hist_data(code, time_before);
        if (d.size):
            close_price = d['close'][0];
            open_price  = d['open'][-1];
            print "Processing " + code + " open: " + str(open_price) + " close: " + str(close_price);
            percent = (close_price - open_price) / open_price;
            if percent < percentage:
                print " OK";
                return True;
        return False;
    return func;


def latest_gain_in_days_range(days, percentage_min, percentage_max):
    now = datetime.datetime.now();
    delta = datetime.timedelta(days=days);
    before = now - delta;
    time_before = before.strftime("%Y-%m-%d");
    def func(code):
        d = ts.get_hist_data(code, time_before);
        if (d.size):
            close_price = d['close'][0];
            open_price = d['open'][-1];
            print "Processing " + code + " open: " + str(open_price) + " close: " + str(close_price);
            percent = (close_price - open_price) / open_price;
            if percent > percentage_min and percent < percentage_max:
                print " OK";
                return True;
        return False;
    return func;
    

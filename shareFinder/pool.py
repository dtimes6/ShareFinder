import datetime;
import tushare as ts;

info = ts.get_stock_basics();

class StockList:
    def __init__(self, l):
        self.__list = l;

    def filter(self, strategy):
        return StockList(filter(strategy, self.__list));

    def println(self):
        for code in self.__list:
            print code + " " + info.name[code];


def get_full_stock_list():
    return StockList(sorted(info.index));

class Strategis:
    def __init__(self):
        self.strategis = [];

    def add(self, strategy):
        self.strategis.append(strategy);

    def extract(self):
        def func(code):
            data = {};
            print ".",
            import sys
            sys.stdout.flush()
            for strategy in self.strategis:
                if (not data.has_key(strategy.ktype)):
                    if (strategy.ktype != 'D'):
                        data[strategy.ktype] = ts.get_hist_data(code=code, ktype=strategy.ktype, autype="qfq");
                    else:
                        data[strategy.ktype] = ts.get_h_data(code=code, autype="qfq");
                    if (isinstance(data[strategy.ktype], type(None))):
                        del data
                        return False;
                if (not strategy.func(data[strategy.ktype])):
                    del data;
                    return False;
            del data;
            print "\n" + code + " " + info.name[code],
            import sys
            sys.stdout.flush()
            return True;
        self.func = func;
        return func;
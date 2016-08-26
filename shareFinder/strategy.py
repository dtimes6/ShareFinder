class Strategy:
    def __init__(self, status):
        self.ktype = status['ktype'];
        start = status['start'];
        end   = status['end'];
        trend = status['trend'];
        op    = status['op'];
        value = status['value'];
        def testing(percent, op):
            if (op == '<'):
                return percent < value;
            if (op == '>'):
                return percent > value;
            return percent < value[1] and percent > value[0];
        def func(code):
            if (code['close'].size <= start): return False;
            if (code['open'].size  <= end):   return False;
            st_val = code['close'][start];
            en_val = code['open'][end];
            percent = (st_val - en_val) / en_val;
            print "close: " + str(st_val) + " open: " + str(en_val) + " percent: " + str(percent);
            if (trend == "drop"):
                percent = -percent;
            return testing(percent, op);
        self.func = func;

class Amount:
    def __init__(self, status):
        self._status = status;
    def greater_than(self, percent):
        self._status["op"] = '>'
        self._status["value"] = percent;
        return Strategy(self._status);
    def less_than(self, percent):
        self._status["op"] = '<'
        self._status["value"] = percent;
        return Strategy(self._status);
    def within(self, range):
        self._status["op"] = '[]'
        self._status["value"] = range;
        return Strategy(self._status);

class Timescale:
    def __init__(self, status):
        self._status = status;
    def days(self):
        self._status["ktype"] = 'D';
        return Amount(self._status);
    def weeks(self):
        self._status["ktype"] = 'W';
        return Amount(self._status);

class Trend:
    def __init__(self, status):
        self._status = status;
    def gain_in(self, amount):
        self._status['trend'] = 'gain';
        self._status['end'] = amount;
        return Timescale(self._status);
    def drop_in(self, amount):
        self._status['trend'] = 'drop';
        self._status['end'] = amount;
        return Timescale(self._status);

def latest():
    return Trend({'start':0});

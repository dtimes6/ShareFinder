from shareFinder.pool import *
from shareFinder.strategy import *

s = Strategis();
s.add(latest().drop_in(30).days().greater_than(0.2))
s.add(latest().gain_in(5).days().greater_than(0.05))
s.extract()

list = get_full_stock_list().filter(s.func);
print "Result:";
list.println();

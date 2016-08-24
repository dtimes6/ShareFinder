import shareFinder.pool as pool;
pool.get_full_stock_list().filter(pool.latest_drop_in_days_greater(15, -0.3))

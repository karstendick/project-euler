def memoize(fn):
    memo={}
    def memoizer(*param_tuple, **kwds_dict):
        if kwds_dict:
            return fn(*param_tuple, **kwds_dict)
        try:
            try:
                return memo[param_tuple]
            except KeyError:
                memo[param_tuple] = result = fn(*param_tuple)
                return result
        except TypeError:
            return fn(*param_tuple)
    return memoizer
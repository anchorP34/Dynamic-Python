# Python Function To Create Python Interval Function
def py_intervals(start, end, interval_between):
    """
        Creates python function of intervals from start to end with the number of intervals between 

        Example:
        - Input: py_intervals(0,101,10)
        - Output: 
            def interval_values(val):
                if val > 0 and val <= 10:
                    return "1-10"
                if val > 10 and val <= 20:
                    return "11-20"
                if val > 20 and val <= 30:
                    return "21-30"
                if val > 30 and val <= 40:
                    return "31-40"
                if val > 40 and val <= 50:
                    return "41-50"
                if val > 50 and val <= 60:
                    return "51-60"
                if val > 60 and val <= 70:
                    return "61-70"
                if val > 70 and val <= 80:
                    return "71-80"
                if val > 80 and val <= 90:
                    return "81-90"
                if val > 90 and val <= 100:
                    return "91-100"
    """
    print('def interval_values(val):')
    intervals = range(start, end, interval_between)
    for idx, val in enumerate(intervals): # Breaks up values from 0 to 100 in 10 different intervals
        if idx == len(intervals) - 1:
            pass
        else:
            print('    if val > {} and val <= {}:'.format(val, intervals[idx + 1]))
            print('\treturn "{}-{}"'.format(val+1, intervals[idx + 1]))

py_intervals(0,101,10)




import solution_2_11

def test_2_11():
    assert 't1' in dir(solution_2_11), "`t1` is not defined"
    t1 = solution_2_11.t1

    assert 't2' in dir(solution_2_11), "`t2` is not defined"
    t2 = solution_2_11.t2
    
    assert 'tdelta' in dir(solution_2_11), "`tdelta` is not defined"
    tdelta = solution_2_11.tdelta
    
    assert 'tdelta_days' in dir(solution_2_11), "`tdelta_days` is not defined"
    tdelta_days = solution_2_11.tdelta_days
    
    assert 'tdelta_seconds' in dir(solution_2_11), "`tdelta_seconds` is not defined"
    tdelta_seconds = solution_2_11.tdelta_seconds
    
    assert tdelta == t2-t1, "Incorrect timespan"
    assert tdelta_days == tdelta.days, "Incorrect number of days"
    assert tdelta_seconds == tdelta.total_seconds(), "Incorrect number of days"
 

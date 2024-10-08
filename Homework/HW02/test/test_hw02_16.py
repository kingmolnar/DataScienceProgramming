
from solution_2_16 import count_levels

def test_2_16():
    result = count_levels('/data/kelleher/MotorInsuranceFraudClaim_MaritalStatus.csv')
    assert '""' in result.keys(), f"Level '""' missing"  
    assert result['""'] == 330, f"Incorrect value for """  
    assert 'Married' in result.keys(), f"Level 'Married' missing"  
    assert result['Married'] == 99, f"Incorrect value for Married"  
    assert 'Single' in result.keys(), f"Level 'Single' missing"  
    assert result['Single'] == 48, f"Incorrect value for Single"  
    assert 'Divorced' in result.keys(), f"Level 'Divorced' missing"  
    assert result['Divorced'] == 23, f"Incorrect value for Divorced" 

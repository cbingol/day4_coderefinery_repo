import pytest
import temperature_plotting as tpl
import os

def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10 # test if the answer is the expected
    assert type(calc) == float # test if the type of the answer is the one expeced
    print(f"calc1 = {calc}")
    
    calc = tpl.compute_mean([-10, 10])
    print(f"calc2 = {calc}")
    assert calc == 0 # test special cases (negative numbers)

    calc = tpl.compute_mean([0,10,0])
    # assert calc == 3.33 # this would fail
    print(f"calc3 = {calc}")
    assert round(calc,4) == 3.3333, "Check that the average is roughly correct" # displays a message if an error
    
    with pytest.raises(TypeError) as e: # asserts that this particular error type will occur
        calc = tpl.compute_mean(["a", "b", "c"]) # this will fail, because the function does not work with strings
    assert not e == None, "We should not be able to average strings"
    
    # calc = tpl.compute_mean([])
    # assert calc == None # this failed in original function definition
    
test_compute_mean()

# integration test
def test_main():
    tpl.main()
    assert os.path.exist("plot_25")
    assert os.path.exist("plot_28")
    


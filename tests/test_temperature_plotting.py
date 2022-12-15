import os
import pytest
import temperature_plotting as tpl
import os
import pytest

# integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")
print("did it finish")

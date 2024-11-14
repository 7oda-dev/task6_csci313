import pytest
from simple_addition_task import add

def test_add():
    
    
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    
    
    with pytest.raises(TypeError):
        add("a", 3)
    with pytest.raises(TypeError):
        add(2, "b")
    with pytest.raises(TypeError):
        add("a", "b")
    with pytest.raises(TypeError):
        add(None, 5)

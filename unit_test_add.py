import pytest
from simple_addition_task import add

def test_add():
  assert add(1, 2) == 3
  assert add(-1, 2) == 1
  assert add(2, -3) == -1
  assert add(-4, -3) == -7
  assert add(0, 1) == 1
  assert add(1, 0) == 1
  assert add(0, 0) == 0
  
  with pytest.raises(TypeError):
    add("a", 3)
  with pytest.raises(TypeError):
    add("a", "b")
  with pytest.raises(TypeError):
    add(None, None)

# test_app.py
from app import add
from app import subtract
from app import multiply
from app import divide

def test_add():    
  assert add(2, 3) == 5

def test_subtract():
  assert subtract(7,5)==2

def test_multiply():
  assert multiply(2,2)==4

def test_divide():
  assert divide(6,3)==2

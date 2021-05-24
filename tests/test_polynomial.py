from polynomials import Polynomial


def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"


@pytest.mark.parametrize(
    "a,b,sum",
    (((0,),(o,1),(0,1)),
    ((2,0,3),(1,2),(3,2,3)),
    ((4,2),(10,2,4),(14,4,4)))

    )   

def test_add(a,b,sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)

def test_add_scalar():
    

def test_equality():
    assert Polynomial    
    
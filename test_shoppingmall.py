import pytest

from Shoppingmall import Electronics, Product


@pytest.fixture
def product():
    return Product("Pen", 10, 5)


@pytest.fixture
def laptop():
    return Electronics("Laptop", 500, 3, 2)


# Product

def test_product_init(product):
    assert product.name == "Pen"
    assert product.price == 10
    assert product.stock == 5


def test_show_details(product, capsys):
    product.show_details()
    out = capsys.readouterr().out
    assert "name: Pen" in out
    assert "price: 10" in out
    assert "stock: 5" in out


def test_buy_reduces_stock_and_returns_total(product):
    assert product.buy(2) == 20
    assert product.stock == 3


def test_buy_entire_stock(product):
    assert product.buy(5) == 50
    assert product.stock == 0


def test_buy_more_than_stock_raises(product):
    with pytest.raises(ValueError, match="Not enough stock"):
        product.buy(6)
    assert product.stock == 5


@pytest.mark.parametrize("quantity", [0, -1, -10])
def test_buy_non_positive_raises(product, quantity):
    with pytest.raises(ValueError, match="greater than zero"):
        product.buy(quantity)
    assert product.stock == 5


# Electronics

def test_electronics_init(laptop):
    assert isinstance(laptop, Product)
    assert laptop.name == "Laptop"
    assert laptop.price == 500
    assert laptop.stock == 3
    assert laptop.warranty == 2


def test_show_warranty(laptop, capsys):
    laptop.show_warranty()
    assert capsys.readouterr().out == "Warranty is for: 2\n"


def test_electronics_buy(laptop):
    assert laptop.buy(1) == 500
    assert laptop.stock == 2


def test_electronics_buy_more_than_stock_raises(laptop):
    with pytest.raises(ValueError):
        laptop.buy(4)
    assert laptop.stock == 3


def test_electronics_buy_negative_raises(laptop):
    with pytest.raises(ValueError):
        laptop.buy(-1)
    assert laptop.stock == 3


def test_extend_warranty(laptop):
    assert laptop.extend_warranty(3) == 5
    assert laptop.warranty == 5


@pytest.mark.parametrize("years", [0, -1])
def test_extend_warranty_non_positive_raises(laptop, years):
    with pytest.raises(ValueError, match="greater than zero"):
        laptop.extend_warranty(years)
    assert laptop.warranty == 2

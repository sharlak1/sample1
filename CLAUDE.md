# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Run all tests: `python -m pytest -v`
- Run a single test: `python -m pytest test_shoppingmall.py::test_buy_entire_stock -v`
- Run the interactive script: `python Shoppingmall.py` (prompts for product name, price, stock, warranty, then a quantity to buy)

pytest is the only dependency; there is no requirements file, build step, or linter configured.

## Architecture

- `Shoppingmall.py` holds everything: `Product` (name, price, stock, `show_details()`, `buy()`), `Electronics(Product)` which adds `warranty` and `show_warranty()`, and `get_int()` for validated integer input.
- `buy()` raises `ValueError` for a quantity that is `<= 0` or greater than stock, leaving stock unchanged; on success it decrements stock, prints the total and remaining stock, and returns the total price. The CLI catches the `ValueError` and prints its message.
- The interactive code must stay under `if __name__ == "__main__":` — the tests import the module, and module-level `input()` calls would break that.
- `test_shoppingmall.py` uses `product` / `laptop` fixtures and `capsys` to check printed output, so changing the printed text of `show_details()` or `show_warranty()` will break tests.

## Conventions

- Keep code beginner-friendly with comments.
- Never add external libraries without asking (pytest is the only dependency).
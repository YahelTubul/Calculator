# Advanced Calculator

A Python based expression calculator supporting arithmetic operations, parentheses, and multiple custom operators including factorial and sum of digits.

---

## Features

- **Arithmetic operations**: +, -, *, /, ^, %
- **Unary operators**: unary minus, negation (~), factorial (!)
- **Advanced operators**: max ($), min (&), average (@), sum of digits (#)

---

## Quickstart

```bash
# Run calculator
python Calculator.py

# Run tests
pytest test_calc.py -v
```

---

## Usage Examples

```text
> 2 + 3 * 4
14.0

> 5!
120.0

> 123#
6.0

> (5 $ 8) & (10 $ 3)
8.0
```

---

## Operators

| Operator | Description       | Example | Result |
|----------|-------------------|---------|--------|
| `+` `-` `*` `/` | Basic arithmetic  | `5 + 3` | `8` |
| `^` | Power             | `2 ^ 3` | `8` |
| `%` | Modulo            | `5 % 3` | `2` |
| `$` `&` `@` | Max, Min, Average | `5 $ 8` | `8` |
| `~` | Nevigation        | `~5` | `-5` |
| `!` | Factorial         | `5!` | `120` |
| `#` | Sum of digits     | `123#` | `6` |

---

## Architecture

```
Input → Tokenizer → Parser → Evaluator → Result
```

Three-stage pipeline:
1. **Tokenizer**: Converts string to tokens
2. **Parser**: Converts infix to prefix notation
3. **Evaluator**: Evaluates prefix expression

---

## Requirements

- Python 3.10+
- Pytest 6.2+
---

## Author

Yahel Haim Tubul
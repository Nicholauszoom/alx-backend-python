# 0x03. Unittests and Integration Tests

## 📘 Description

This project is part of the ALX Backend Python curriculum. It focuses on writing **unit tests** and **integration tests** to ensure code correctness, maintainability, and reliability. You will learn best practices around writing test cases using `unittest`, `parameterized`, and `mock` libraries in Python.

## 🧪 Learning Objectives

- Understand the importance of testing in software development
- Write unit tests for Python functions
- Use `unittest.TestCase` to structure your test cases
- Parameterize tests with `@parameterized.expand`
- Mock external calls with `unittest.mock`
- Perform integration testing

## 🛠️ Requirements

- Python 3.x
- Use only standard Python libraries and the `parameterized` module
- Follow PEP8 style

## 📁 Files

| File | Description |
|------|-------------|
| `utils.py` | Contains utility functions like `access_nested_map()` |
| `test_utils.py` | Unit tests for `utils.py`, including parameterized tests |
| `client.py` | (Later tasks) Contains a client class that makes HTTP calls |
| `test_client.py` | (Later tasks) Unit and integration tests for the client class |

## 🔍 Example Task: Testing `access_nested_map`

This function retrieves a value from a nested dictionary using a tuple path. Example:

```python
access_nested_map({"a": {"b": 2}}, ("a", "b"))  # Returns 2

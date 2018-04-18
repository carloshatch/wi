#!/bin/bash

# Very minimal tests, just checking basic commands. It's difficult to check
# what the result should be as it depends on the platform is executed

# Basic usage
wi

# Adding an index url
wi --index-url=https://pypi.python.org/simple

# Using a wrong index
wi --index-url=https://pypi.python.org/badindex

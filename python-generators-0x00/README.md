# Python Generators Project

A Python project demonstrating the use of generators for efficient data streaming and batch processing from a MySQL database.

## Project Description

This project implements various generator patterns to handle large datasets efficiently by:
- Streaming user data one record at a time
- Processing users in configurable batch sizes
- Implementing lazy pagination
- Computing statistics using generators

## Features

- Database connection and setup
- Stream individual user records
- Batch processing with configurable sizes
- Lazy pagination implementation
- Age statistics computation using generators

## Requirements

- Python 3.x
- MySQL Server
- mysql-connector-python

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install mysql-connector-python
```

3. Configure MySQL connection in `seed.py`:
```python
host='localhost'
user='root'
password=''
```

## Project Structure

- `seed.py` - Database initialization and data seeding
- `0-stream_users.py` - Single record streaming implementation
- `1-batch_processing.py` - Batch processing implementation
- `2-lazy_paginate.py` - Lazy pagination implementation
- `4-stream_ages.py` - Age statistics computation
- `user_data.csv` - Sample dataset

## Usage

### Initialize Database
```bash
python 0-main.py
```

### Stream Individual Users
```bash
python 1-main.py
```

### Process Users in Batches
```bash
python 2-main.py
```

### Use Lazy Pagination
```bash
python 3-main.py
```

### Compute Average Age
```bash
python 4-stream_ages.py
```

## Implementation Details

### Streaming Users
```python
def stream_users():
    """Generator to stream user records one at a time"""
    # Implementation in 0-stream_users.py
```

### Batch Processing
```python
def stream_users_in_batches(batch_size):
    """Generator to stream users in batches"""
    # Implementation in 1-batch_processing.py
```

### Lazy Pagination
```python
def lazy_pagination(page_size):
    """Generator for lazy pagination"""
    # Implementation in 2-lazy_paginate.py
```

### Age Statistics
```python
def stream_user_ages():
    """Generator to stream user ages"""
    # Implementation in 4-stream_ages.py
```
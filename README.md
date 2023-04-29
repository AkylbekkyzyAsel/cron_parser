# cron_parser

- This project contains a script for parsing cron expressions and displaying the corresponding schedule, as well as unit tests for the script.

### Requirements

- Python 3.0 or greater

### Installation

1. Clone the repository to your local machine:

```
$ git clone https://github.com/your-username/cron-parser.git
```

2. Change into the project directory:

```
$ cd cron-parser
```

3. Install required dependencies:

```
$ pip install -r requirements.txt
```

### Usage

The `cron_parser.py` script takes a single command-line argument: a cron expression in the standard format with five time fields (minute, hour, day of month, month, and day of week) plus a command, and expands each field to show the times at which it will run. 

Here's an example usage:

```
$ python cron_parser.py '*/15 0 1,15 * 1-5 /usr/bin/find'
```

This will output the schedule corresponding to the given cron expression in a table format.

### Running tests

To run the unit tests, run the following command:

```
$ python -m unittest test_cron_parser.py
```

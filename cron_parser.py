import sys

def func_hyphen(field):
    parts = field.split('/')
    increment = 1
    start = int(parts[0].split('-')[0])
    end = int(parts[0].split('-')[1])
    if '/' in field:
        increment = int(parts[1])
    return set(i for i in range(start, end + 1, increment))


def func_slash(field, limit_end):
    parts = field.split('/')
    start = 0
    increment = int(parts[1])
    if parts[0] != '*':
        start = int(parts[0])
        limit_end = start
    return set(i for i in range(start, limit_end + 1, increment))


def parse_field(field, limit_start, limit_end):

    result = set()

    if field == '*':
        result.update(range(limit_start, limit_end + 1))

    elif '-' in field:
        field_list = field.split(',')
        result = func_hyphen(field_list[0])
        if len(field_list) > 1:
            result.update(field_list[1:])

    elif '/' in field:
        field_list = field.split(',')
        result = func_slash(field_list[0], limit_end)
        if len(field_list) > 1:
            result.update(field_list[1:])

    elif ',' in field:
        result = set(int(i) for i in field.split(','))

    else:
        result.add(int(field))

    return sorted(result)


def expand_cron(cron_string):

    minute, hour, dom, month, dow, command = cron_string.split()

    minute_values = parse_field(minute, 0, 59)
    hour_values = parse_field(hour, 0, 23)
    dom_values = parse_field(dom, 1, 31)
    month_values = parse_field(month, 1, 12)
    dow_values = parse_field(dow, 0, 6)

    print("{:<14}{}".format('minute', ' '.join(str(i) for i in minute_values)))
    print("{:<14}{}".format('hour', ' '.join(str(i) for i in hour_values)))
    print("{:<14}{}".format('day of month', ' '.join(str(i) for i in dom_values)))
    print("{:<14}{}".format('month', ' '.join(str(i) for i in month_values)))
    print("{:<14}{}".format('day of week', ' '.join(str(i) for i in dow_values)))
    print("{:<14}{}".format('command', command))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py '<cron-string>'")
        sys.exit(1)

    cron_string = sys.argv[1]
    expand_cron(cron_string)

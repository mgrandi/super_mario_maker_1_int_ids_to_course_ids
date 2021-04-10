# super_mario_maker_1_int_ids_to_course_ids

a quick script to convert super mario maker 1 integer IDs to the course IDs you see in game

see this page for more information: https://github.com/kinnay/NintendoClients/wiki/SMM-Code-Generation

## setup

this requires `poetry`:

```plaintext

# not in a virtualenv, install this system/user wide
pip3 install poetry --user

cd super_mario_maker_1_int_ids_to_course_ids

poetry shell

poetry install

```

## usage

```plaintext
> python cli.py --help
usage: cli.py [-h] [--log-to-file-path LOG_TO_FILE_PATH] [--verbose] [--no-stdout] --id-list ID_LIST

scrape the playstation games site

optional arguments:
  -h, --help            show this help message and exit
  --log-to-file-path LOG_TO_FILE_PATH
                        log to the specified file
  --verbose             Increase logging verbosity
  --no-stdout           if true, will not log to stdout
  --id-list ID_LIST     ID list, one per line

```


## example

```plaintext

> python cli.py --id-list .\course_id_lists\test.txt

2021-04-10T13:08:40.194136-07:00 INFO    : ########### STARTING ###########
2021-04-10T13:08:40.196175-07:00 INFO    : results:

SMM1::4005199::77A9-0000-003D-1D4F

2021-04-10T13:08:40.197150-07:00 INFO    : Done!

```
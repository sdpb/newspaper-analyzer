# Newspaper analyzer

Given a newspaper URL, a quantity of news items to analyze, and the original newspaper's language (two letters),
this script returns the positive or negative score of each news item with its amount of
subjectivity.

*NOTE:* Due to the computational requirement, is recommended to select a little amount of news.

### Use

```bash
python3 scraper.py <NEWSPAPER URL> <AMOUNT OF NEWS> <NEWSPAPER'S LANGUAGE>
```

To see language options and general help to know more about the script usage

```bash
python3 scraper.py [-h | --help]
```

### Example

```bash
python3 scraper.py "https://www.eltiempo.com/" 5 es
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

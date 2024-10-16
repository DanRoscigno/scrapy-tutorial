# Using Scrapy to verify documentation URLs

The Cloud console links to the docs, as we rearrange the docs URLs change.

Goal is to detect redirects and 404's 

By default, scrapy misses `meta refresh` redirects, although they show in the debug log:

```bash
[scrapy.downloadermiddlewares.redirect]
DEBUG: Redirecting (meta refresh) to <GET https://newURL/> from <GET https://oldURL>
```

This
1. cleans up the output and log
2. checks the links in `doc_urls.txt` (hardcoded filename)
3. generates a CSV file named `x.csv` with any redirected pages
4. pops the debug log in a file named `log`

```bash
rm x.csv log && scrapy crawl quotes -o x.csv >log  2>&1
```

This gives a list of non-200 results and meta-refresh redirects
(we use meta refresh to the landing page for 404's):

```bash
grep -e "DEBUG: Crawled" -e "DEBUG: Redirecting" log| grep -v "(200)" > errors
```

Next we need to check the file `errors` for size. If the file is zero bytes,
then there are no errors. If it is more than zero bytes, then we need to:

1. Send the content of file `errors` to the Summary so that we know which URLs are bad
2. Set the CI check to an error condition (probably `exit 1`)

# scrapy-tutorial

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

This gives a list of non-200 results or meta-refresh redirects (we use meta refresh to the landing page for 404's):

```bash
grep -e "DEBUG: Crawled" -e "DEBUG: Redirecting" log| grep -v "(200)"
```


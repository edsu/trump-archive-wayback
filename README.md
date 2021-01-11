# trump-archive-wayback

This repository contains a dataset that maps Trump's tweets to their
representations in the Internet Archive's [Wayback Machine]. It uses the [Trump
Archive] CSV export to look for each tweet in Internet Archive's [CDX API]. Care
is taken to only match tweet URLs while allowing for URLs that use various query
parameters. The snapshots directory contains a JSON file for each tweet id which
contains all the archival snapshots.

I had initially tried to discover the tweet ids by using the CDX API's
`matchType=prefix` functionality. But the CDX API didn't seem to be returning
all the results that are available. You can see this initial experimentation in
[this Jupyter notebook].

## Run

    pip install -r requirements.txt
    ./fetch.py

[Trump Archive]: https://www.thetrumparchive.com/

[Wayback Machine]: https://web.archive.org

[CDX API]: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server

[this Jupyter notebook]: https://github.com/edsu/notebooks/blob/master/Trump%20Tweets%20at%20Internet%20Archive.ipynb

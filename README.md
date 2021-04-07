## Redadocs - Some Tools for Redash, producing Docs, etc.

Makes working with [Redash](https://redash.io/) lots of fun! Generate
docs in CSV/Markdown with a few commands, a list of the dashboards,
queries, rename thing in bulk...

### Take Advantage of some documentation

In addition to the metadata already in redash (creation date, name, tags,...)
you can add a "text widget" to a dashboard with additional information,
if you:

1.  add a @description tag somewhere and then include your data in brackets:
2.  <publicLink> to add the public link </publicLink>
3.  <description> to generate a description column </description>

### Minimal usage example 
to produce a CSV list of dashboardse use something like:

1. source .env (or export your keys by hand) containing your API Key + Url
2. python examples/output_to_csv.py

>> should produce an output.csv containing all your dashboards.

## Redadocs - Some Tools for Redash, producing Docs, etc.

Makes working with [Redash](https://redash.io/) lots of fun! Generate
docs in CSV/Markdown with a few commands, a list of the dashboards,
queries, rename thing in bulk...

### Setup whatever
This project is a ./go project; To run anything in this project,
you only need the batect requisites, Docker & a JVM. Then: 

```shell

$ ./batect --list-tasks
Utility tasks:
- dep: Installs dependencies via pipenv
- run_csv_output: Auto sources your .env file, then runs the CSV output inside docker.
- shell: Start a shell in the development environment.
- test: Runs the tests inside docker.

...

$ ./batect run_csv_output


...
Loading .env environment variables...


Loading .env environment variables...
 Connecting to https://.../ using API key XXX...

run_csv_output finished with exit code 0 in 11.5s.

```

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

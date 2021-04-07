def get_db_count(db_dict):
    return db_dict["count"]

def get_db_overview(client):
    """

    Args:


    Returns:

    """
    db_count = get_db_count(client.db_dict)
    return f"Dashboard Count: {db_count}\n"

def get_all_db_details(client, csv=False):
    dashboards = client.dashboards(page=1,page_size=client.dashboards()["count"])
    details = []
    for i in range(0,dashboards["count"]):
        details.append(get_db_details(client, dashboards["results"][i], csv))
    return details

def get_db_details(client, db_result, csv=False):

    descr_block = get_slug_description(client, db_result["slug"])

    description = get_substring_between(descr_block, "<description>", "</description>")
    public_link = get_substring_between(descr_block,"<publicLink>","</publicLink>")

    details =[db_result['name'],db_result['tags'],
              db_result['updated_at'], db_result['is_archived'], description, public_link
              ]

    return details

def get_substring_between(s, beg_marker, end_maker):

    if s.find(beg_marker) and s.find(end_maker):
        start = s.find(beg_marker) + len(beg_marker)
        end = s.find(end_maker)
        substring = s[start:end]
    else: substring = ""
    return substring

def get_slug_description(client, slug):
    db = client.dashboard(slug)

    result = ""
    wg = db.get("widgets", [])
    for item in wg:
        if "text" in item:
            if "@Description" in item["text"]:
                result = item["text"]
    return result

def get_public_link(client, slug):
    db = client.dashboard(slug)

    result = ""
    wg = db.get("widgets", [])
    for item in wg:
        if "text" in item:
            if "@Metadata" in item["text"]:
                metadata = item["text"]
                link = metadata
    return result

def get_db_list(client):
    count = client.dashboards()["count"]
    dbs = client.dashboards(page_size=count)
    names = []
    slugs = []
    for row in dbs["results"]:
        names.append(row["name"])
        slugs.append(row["slug"])

    return slugs, names

def update_db_list(client, list_to_update):
    slugs,names = list_to_update
    i=0
    for slug in slugs:
        db_probs = client.dashboard(slug)
        print(names[i])
        print(db_probs["id"])
        client.update_dashboard(dashboard_id=db_probs["id"], properties={"name": names[i]})
        i+=1
    return 0
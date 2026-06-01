def count_records(data):
    return len(data)

def extract_titles(data):
    return [item.get("title") for item in data]

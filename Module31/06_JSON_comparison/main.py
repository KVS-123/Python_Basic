import json

def search(data, target):
    if isinstance(data, dict):
        if target in data:
            return data[target]
        for value in data.values():
            result = search(value, target)
            if result is not None:
                return result
    elif isinstance(data, list):
        for i in data:
            result = search(i, target)
            if result is not None:
                return result
    return None


diff_list = ["services", "staff", "datetime"]

with open('json_old.json', 'r', encoding='utf-8') as f1:
    old_json_file = json.load(f1)

with open('json_new.json', 'r', encoding='utf-8') as f2:
    new_json_file = json.load(f2)

result_dict = {}

for i in diff_list:
    old_val = search(old_json_file, i)
    new_val = search(new_json_file, i)
    if new_val != old_val:
        result_dict[i] = new_val

with open("result.json", "w", encoding='utf-8') as f3:
    json.dump(result_dict, f3, indent=4)

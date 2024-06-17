import plyvel
import os
import json

def fetch_values_from_leveldb(db_path):
    db = plyvel.DB(db_path, create_if_missing=False)
    data = {}
    for key, value in db:
        try:
            key_str = key.decode('utf-8')
            value_str = value.decode('utf-8')
            data[key_str] = value_str
        except UnicodeDecodeError:
            pass  # Handle non-UTF-8 encoded data if necessary
    db.close()
    return data

def main():
    # Adjust the path as necessary
    db_path = os.path.expanduser('~/.config/google-chrome/Default/Local Extension Settings/<Extension ID>')
    values = fetch_values_from_leveldb(db_path)
    print(json.dumps(values, indent=2))

if __name__ == "__main__":
    main()

import json

class to_dump:
    def __init__(self,data,file):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

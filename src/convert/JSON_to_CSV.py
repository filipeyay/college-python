import json

if __name__ == "__main__":
    try:
        with open("path_to_file.json", "r") as f:
            data = json.loads(f.read())
        converted = ",".join([*data[0]])
        for obj in data:
            converted += f'\n{obj["info_ONE"]}, {obj["info_TWO"]}, {obj["info_THREE"]}'
        with open("converted.csv", "w") as f:
            f.write(converted)
    except Exception as ex:
        print(f"Error: {str(ex)}")

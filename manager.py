import json
import message


class JsonManager:
    def load(self, file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data

    def dump(self, data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file)


class InputManager:
    def must_be_string(self, value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError(message.string)

    def must_be_int(self, value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError(message.integer)

#static Method
# so we dont have to create an instance or state in classs 

class ChaiUtils:
    # @staticmethod
    def clean_string(text):
        return [item.strip() for item in text.split(",")]

raw = "water ,  milk ,  ginger, honey"

obj = ChaiUtils()
text = obj.clean_string(raw)
print(text)

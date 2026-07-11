from client import ProductSpecTranslationClient
client = ProductSpecTranslationClient()
print(client.translate_specs({"weight": 10}, "en", "zh"))
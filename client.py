class ProductSpecTranslationClient:
    def translate_specs(self, dimensions: dict, source_language: str, target_language: str) -> dict:
        return {"translated_specifications": {k: f"{v} translated" for k, v in dimensions.items()}}
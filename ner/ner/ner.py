import spacy
from spacy import Language, displacy

from .models import Entity, NERRequest, NERResult


class Processor:
    """
    This class is used to hold the processing logic, the main value is being able to control the spacy loading lifecycle.
    """

    def __init__(self):
        self.nlp: Language = spacy.load("en_core_web_sm")

    def extract_ner(self, request: NERRequest) -> NERResult:
        doc = self.nlp(request.text)

        return NERResult(
            entities=[
                Entity(id=ent.ent_id, text=ent.text, label=ent.label_)
                for ent in doc.ents
            ],
            html=displacy.render(doc, style="ent", minify=True, page=True),
        )

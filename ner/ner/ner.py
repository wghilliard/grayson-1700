import spacy
from spacy import Language, displacy

from .models import Entity, NERRequest, NERResult


class Processor:
    def __init__(self):
        self.nlp: Language = spacy.load("en_core_web_sm")

    def extract_ner(self, request: NERRequest) -> NERResult:
        """
        TODO - request validation
        :param request:
        :return:
        """

        doc = self.nlp(request.text)

        result = NERResult(
            entities=[Entity(text=ent.text, label=ent.label_) for ent in doc.ents],
            html=displacy.render(doc, style="dep", minify=True, page=True),
        )

        return result

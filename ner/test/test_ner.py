from typing import NoReturn

from pytest import fixture

from ner import NERRequest as Request, NERResult as Result
from ner.ner import Processor


@fixture
def processor():
    return Processor()


def test_get_ner__valid_input(processor: Processor) -> NoReturn:
    text = "Apple is looking at buying U.K. startup for $1 billion"

    # given: some text, limit?
    # return:
    # - a dict w/ the NER values
    # - a string representing the html
    # - errors, if any
    # - runtime stats
    result: Result = processor.extract_ner(Request(text=text))

    assert result.entities is not None
    assert len(result.entities) > 0

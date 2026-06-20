
from pydantic import BaseModel, Field, RootModel
from typing import List, Optional, Dict, Any, Union
from enum import Enum

class Metadata(BaseModel):
    summary: List[str] = Field(default_factory=list, description="A concise summary of the document's content.")
    Title: str
    Authors: str
    DateCreated: str
    LastModifiedDate: str
    Publisher: str
    Language: str
    pageCount: Union[int, str]
    SentimentTone: str


class ChangeFormat(BaseModel):
    Page : str
    changes : str

class SummaryResponse(RootModel[list[ChangeFormat]]):
    pass

class PromptType(str, Enum):
    DOCUMENT_ANALYSIS = "document_analysis"
    DOCUMENT_COMPARISON = "document_comparison"
    CONTETUALIZE_QUESTION = "contextualize_question"
    CONTEXT_QA = "context_qa"






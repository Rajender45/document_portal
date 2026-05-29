
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyse and summarise documents.
Return ONLY valid JSON matching the exact schema below.

{format_instructions}
Analyse this document:
                                          
{document_text}
"""
)
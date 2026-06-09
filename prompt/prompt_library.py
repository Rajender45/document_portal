
from langchain_core.prompts import ChatPromptTemplate

document_analysis_prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyse and summarise documents.
Return ONLY valid JSON matching the exact schema below.

{format_instructions}
Analyse this document:
                                          
{document_text}
"""
)

document_comparison_prompt = ChatPromptTemplate.from_template("""
You will be provided with content from two PDFs. Your tasks are as follows:
                                                              
1. Compare the content in two PDFs.
2. Identify the difference in PDF and note down the page number.
3. The output you provide must be page wise comparison content
4. If any page do not have any change, mention as 'NO CHANGE'
                                                              
Input documnets:
                                                              
{combined_docs}
                                                              
Your response should this format:
                                                              
{format_instructions}
"""
)


PROMPT_REGISTRY = {"document_analysis": document_analysis_prompt, "document_comparison": document_comparison_prompt}
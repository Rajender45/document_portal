# Testing code for document analysis 
# import os
# from pathlib import Path
# from src.document_analyzer.data_ingestion import DocumnetHandler
# from src.document_analyzer.data_analyser import DocumentAnalyzer

# PDF_PATH = r"D:\LLMOps\document_portal\data\document_analysis\Resume.pdf"


# class DummyFile:
#     def __init__(self, file_path):
#         self.name = Path(file_path).name
#         self._file_path = file_path

#     def getbuffer(self):
#         return open(self._file_path, 'rb').read()
    
# def main():

#     try:
#         dummy_pdf = DummyFile(PDF_PATH)

#         handler = DocumnetHandler(session_id="test_ingestion_analysis")

#         saved_path=handler.save_pdf(dummy_pdf)
#         print(f"PDF saved at: {saved_path}")

#         text_content = handler.read_pdf(saved_path)
#         print(f"Extracted Text length: {len(text_content)} chars\n")
        
#         print("Starting metadata analysis...")
#         analyzer = DocumentAnalyzer()

#         analysis_result = analyzer.analyze_document(text_content)

#         print("\n=== METADATA ANALYSIS RESULT ===")
#         for key, value in analysis_result.items():
#             print(f"{key}: {value}")
    
#     except Exception as e:
#         print(f"Test failed: {e}")

# if __name__ == "__main__":
#     main()
        
#           # Print the first 500 characters

# Testing code for document compare

# import io
# from pathlib import Path
# from src.document_compare.data_ingestion import DocumentIngestion
# from src.document_compare.document_comparator import DocumentComparatorLLM


# def load_fake_uploaded_file(file_path: Path):
#     return io.BytesIo(file_path.read_bytes())

# def test_compare_documents():
#     ref_path= Path("D:\\LLMOps\\document_portal\\data\\document_compare\\AgenticAI_v1.pdf")
#     act_path = Path("D:\\LLMOps\\document_portal\\data\\document_compare\\AgenticAI_v2.pdf")

#     class FakeUpload:
#         def __init__(self, file_path: Path):
#             self.name = file_path.name
#             self._buffer = file_path.read_bytes()


#         def getbuffer(self):
#             return self._buffer
        
#     comparator = DocumentIngestion()
#     ref_upload = FakeUpload(ref_path)
#     act_upload = FakeUpload(act_path)


#     ref_file, act_file = comparator.save_uploaded_files(ref_upload, act_upload)
#     combined_text = comparator.combine_documents()
#     comparator.clean_old_session(keep_latest=3)

#     print("\n Combined Text Preview (First 500 chars):\n")
#     print(combined_text[:500])


#     llm_comparator = DocumentComparatorLLM()
#     df = llm_comparator.compare_documents(combined_text)

#     print("\n Document Comparison Result:\n")
#     print(df) 

# if __name__ == "__main__":
#     test_compare_documents()

# testing code for document chat functionality

import sys
from pathlib import Path
from langchain_community.vectorstores import FAISS
from src.single_document_chat.data_ingestion import SingleDocIngestor
from src.single_document_chat.retrieval import ConversationalRAG
from utils.model_loader import ModelLoader

FAISS_INDEX_PATH = Path("faiss_index")



def test_conversational_rag_on_pdf(pdf_path:str, question:str):
    try:
        model_loader = ModelLoader()

        if FAISS_INDEX_PATH.exists():
            print("Loading existing FAISS index...")
            embeddings = model_loader.load_embeddings()
            vectorstore = FAISS.load_local(folder_path=str(FAISS_INDEX_PATH), embeddings= embeddings, allow_dangerous_deserialization=True)
            retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
        else:
            print("FAISS index not found. Ingesting PDF and creating index...")
            with open(pdf_path, "rb") as f:
                uploaded_files = [f]
                ingestor = SingleDocIngestor()
                retriever = ingestor.ingest_files(uploaded_files)
        print("Running Conversational RAG...")
        session_id = "test_conversational_rag"
        rag = ConversationalRAG(retriever=retriever, session_id = session_id)

        response = rag.invoke(question)
        print(f"\nQuestion: {question}\nAnswer: {response}")
                  


    except Exception as e:
        print(f"test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":

    pdf_path = r"D:\\LLMOps\\document_portal\\data\\single_document_chat\\Resume.pdf"
    question = "what is the main topic of the document?"

    if not Path(pdf_path).exists():
        print(f"PDF file does not exist at {pdf_path}")
        sys.exit(1)

    test_conversational_rag_on_pdf(pdf_path, question)


        


     
 



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



import io
from pathlib import Path
from src.document_compare.data_ingestion import DocumentIngestion
from src.document_compare.document_comparator import DocumentComparatorLLM


def load_fake_uploaded_file(file_path: Path):
    return io.BytesIo(file_path.read_bytes())

def test_compare_documents():
    ref_path= Path("D:\\LLMOps\\document_portal\\data\\document_compare\\AgenticAI_v1.pdf")
    act_path = Path("D:\\LLMOps\\document_portal\\data\\document_compare\\AgenticAI_v2.pdf")

    class FakeUpload:
        def __init__(self, file_path: Path):
            self.name = file_path.name
            self._buffer = file_path.read_bytes()


        def getbuffer(self):
            return self._buffer
        
    comparator = DocumentIngestion()
    ref_upload = FakeUpload(ref_path)
    act_upload = FakeUpload(act_path)


    ref_file, act_file = comparator.save_uploaded_files(ref_upload, act_upload)
    combined_text = comparator.combine_documents()
    comparator.clean_old_session(keep_latest=3)

    print("\n Combined Text Preview (First 500 chars):\n")
    print(combined_text[:500])


    llm_comparator = DocumentComparatorLLM()
    df = llm_comparator.compare_documents(combined_text)

    print("\n Document Comparison Result:\n")
    print(df) 

if __name__ == "__main__":
    test_compare_documents()


        


     
 


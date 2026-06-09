
import os
from pathlib import Path
from src.document_analyzer.data_ingestion import DocumnetHandler
from src.document_analyzer.data_analyser import DocumentAnalyzer

PDF_PATH = r"D:\LLMOps\document_portal\data\document_analysis\Resume.pdf"


class DummyFile:
    def __init__(self, file_path):
        self.name = Path(file_path).name
        self._file_path = file_path

    def getbuffer(self):
        return open(self._file_path, 'rb').read()
    
def main():

    try:
        dummy_pdf = DummyFile(PDF_PATH)

        handler = DocumnetHandler(session_id="test_ingestion_analysis")

        saved_path=handler.save_pdf(dummy_pdf)
        print(f"PDF saved at: {saved_path}")

        text_content = handler.read_pdf(saved_path)
        print(f"Extracted Text length: {len(text_content)} chars\n")
        
        print("Starting metadata analysis...")
        analyzer = DocumentAnalyzer()

        analysis_result = analyzer.analyze_document(text_content)

        print("\n=== METADATA ANALYSIS RESULT ===")
        for key, value in analysis_result.items():
            print(f"{key}: {value}")
    
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    main()
        
          # Print the first 500 characters


import uuid
from pathlib import Path
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader


class SingleDocIngestion:
    def __init__(self):
        try:
            self.log = CustomLogger.get_logger(__name__)

        except Exception as e:
            self.log.error("Failed to initialize ")


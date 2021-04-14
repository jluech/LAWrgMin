# To use textract package install poppler
conda install -c conda-forge poppler
pip install textract
import textract

# Function to read PDF, Word or HTML Documents 
def get_text(filepath):
    text = textract.process(filepath)
    return text.decode('utf8')
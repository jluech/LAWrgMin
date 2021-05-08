import logging
import sys
import os

import textract

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_root.log")

default_in_directory = "./data_static"  # default input, adjustable by providing args
default_out_directory = "./targer_instance/data/in"


# function to read .pdf, .docx or .html files; requires absolute file path
def extract_text(filepath, out_directory):
    logging.debug("Extracting text from file %s", filepath)

    filename = ".".join(filepath.split("/")[-1].split(".")[:-1])
    output_path = "{__outdir}/{__name}.txt".format(__outdir=os.path.abspath(out_directory), __name=filename)
    if os.path.exists(output_path):
        os.remove(output_path)

    text = textract.process(filepath)
    decoded = text.decode('utf8')
    with open(output_path, "x") as file:
        file.write(decoded)


if __name__ == "__main__":
    args = sys.argv[1:]  # ignore first arg as it's the script
    if args.__len__() > 0:
        in_path = default_in_directory
        out_dir = default_out_directory
        if args.__contains__("-i"):
            in_path = os.path.abspath(args[args.index("-i") + 1])
            logging.debug("Extracting text from %s", in_path)
        if args.__contains__("-o"):
            out_dir = os.path.abspath(args[args.index("-o") + 1])
            logging.debug("Saving extracted text to %s", out_dir)

        if os.path.isdir(in_path):
            for file in os.listdir(in_path):
                extract_text(os.path.join(in_path, file), out_dir)
        else:
            extract_text(in_path, out_dir)
    else:
        files = [f for f in os.listdir(default_in_directory) if not f.startswith(".")]  # filter hidden files
        origin_dir = os.path.abspath(os.curdir)
        os.chdir(default_in_directory)
        for file in files:
            extract_text("{__abs}/{__file}".format(__abs=os.path.abspath(os.curdir), __file=file), default_out_directory)
        os.chdir(origin_dir)

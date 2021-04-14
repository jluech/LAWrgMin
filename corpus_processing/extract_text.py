import sys
import os

import textract

default_directory = "../data_static"  # default input, always output


# function to read .pdf, .docx or .html files; requires absolute file path
def extract_text(filepath):
    text = textract.process(filepath)
    decoded = text.decode('utf8')

    filename = ".".join(filepath.split("/")[-1].split(".")[:-1])
    output_path = "{__outdir}/{__name}.txt".format(__outdir=os.path.abspath(default_directory), __name=filename)
    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, "x") as file:
        file.write(decoded)


if __name__ == "__main__":
    args = sys.argv[1:]  # ignore first arg as it's the script
    if args.__len__() > 0:
        if args.__len__() > 1:
            for file in args:
                extract_text(os.path.abspath(file))
        else:
            extract_text(os.path.abspath(args[0]))
    else:
        files = [f for f in os.listdir(default_directory) if not f.startswith(".")]  # filter hidden files
        origin_dir = os.path.abspath(os.curdir)
        os.chdir(default_directory)
        for file in files:
            extract_text("{__abs}/{__file}".format(__abs=os.path.abspath(os.curdir), __file=file))
        os.chdir(origin_dir)

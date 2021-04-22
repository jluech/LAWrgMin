import os
import subprocess
import sys

targer_main_file = "main.py"
targer_files_dir = "data/NER/CoNNL_2003_shared_task"
# targer_files_dir = "data/NER/ECHR"
train_file = "/".join([targer_files_dir, "train.txt"])
dev_file = "/".join([targer_files_dir, "dev.txt"])
test_file = "/".join([targer_files_dir, "test.txt"])

data_formatting = "connl-ner-2003"
evaluation_type = "f1-alpha-match-10"
epochs = "10"  # min-epochs is 50 by default


def prepare_echr_files():
    orig_dir = os.getcwd()
    os.makedirs(targer_files_dir, exist_ok=True)

    number_of_files = 6
    for idx in range(number_of_files):
        idx_two_digit = idx if idx >= 10 else "0"+str(idx)
        os.chdir("../../corpus_processing/out/{__idx}/".format(__idx=idx_two_digit))
        with open("{__idx}.conll".format(__idx=idx_two_digit), "r") as echr_file:
            content = echr_file.read()
            choice = idx % 3
            if choice == 0:
                file_dir = "/".join([orig_dir, "lstm", "/".join(train_file.split("/")[:-1])])
                file_name = "train.txt"
            elif choice == 1:
                file_dir = "/".join([orig_dir, "lstm", "/".join(dev_file.split("/")[:-1])])
                file_name = "dev.txt"
            else:
                file_dir = "/".join([orig_dir, "lstm", "/".join(test_file.split("/")[:-1])])
                file_name = "test.txt"
            os.makedirs(file_dir, exist_ok=True)
            os.chdir(file_dir)
            append_write = "a" if os.path.exists("./"+file_name) else "x"
            with open(file_name, append_write) as file:
                file.write(content)
        os.chdir(orig_dir)


if __name__ == "__main__":
    args = sys.argv[1:]  # ignore first arg as it's the script
    if args.__len__() > 0 and args.__contains__("--prepare"):
        prepare_echr_files()

    os.chdir("lstm")  # need to call it relative to the main file
    # so other files being loaded during the process have the correct working directory

    subprocess.run(["python", targer_main_file, "--train", train_file, "--dev", dev_file, "--test", test_file,
                    "-d", data_formatting, "--evaluator", evaluation_type, "-e", epochs, "--opt", "adam",
                    "--lr", "0.001", "--save-best", "yes", "--patience", "20", "--rnn-hidden-dim", "200",
                    "--gpu", "-1"])
    os.chdir("..")

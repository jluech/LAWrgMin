import subprocess
import os

targer_main_file = "main.py"
train_file = "data/NER/CoNNL_2003_shared_task/train.txt"
dev_file = "data/NER/CoNNL_2003_shared_task/dev.txt"
test_file = "data/NER/CoNNL_2003_shared_task/test.txt"
data_formatting = "connl-ner-2003"
evaluation_type = "f1-alpha-match-10"
epochs = "10"  # min-epochs is 50 by default

if __name__ == "__main__":
    os.chdir("lstm")  # need to call it relative to the main file
    # so other files being loaded during the process have the correct working directory
    subprocess.run(["python", targer_main_file, "--train", train_file, "--dev", dev_file, "--test", test_file,
                    "-d", data_formatting, "--evaluator", evaluation_type, "-e", epochs, "--opt", "adam",
                    "--lr", "0.001", "--save-best", "yes", "--patience", "20", "--rnn-hidden-dim", "200",
                    "--gpu", "-1"])
    os.chdir("..")

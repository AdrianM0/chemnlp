import pandas as pd
from huggingface_hub import hf_hub_download
import regex as re

DATA = "uniprot_sentences"

def clean_up_sentences(text : str) -> str:
    "Remove (By similarity) from the sentences"
     
    updated_text = re.sub(r'\s*\((?:By\.? similarity)\)\s*', '', text)
    updated_text = updated_text.replace(" . ", ". ")
    return updated_text


def load_dataset() -> pd.DataFrame:
    uniprot = hf_hub_download(
        repo_id="chemnlp/uniprot",
        filename=f"{DATA}/data_clean.csv",
        repo_type="dataset",
    )

    uniprot = pd.read_csv(uniprot)
    uniprot.sentences = uniprot.sentences.apply(clean_up_sentences)
    uniprot.to_csv("data_clean.csv", index=False)
    print(f"Successfully loaded {DATA}!")
    return uniprot


if __name__ == "__main__":
    load_dataset()

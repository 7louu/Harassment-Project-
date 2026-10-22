import sys
from pathlib import Path
from data.preprocessing import df
from repository import MongoRepository

SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def upload_dataset():
    with MongoRepository() as repository:
        return repository.save_dataset(df)


if __name__ == "__main__":
    print(upload_dataset())

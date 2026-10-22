from config import DatabaseConfig, get_database_config
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import pandas as pd
from typing import Optional



class MongoRepository:
    def __init__(self, config: Optional[DatabaseConfig] = None) -> None:
        self.config = config or get_database_config()
        self.client = None

        try:
            self.client = MongoClient(self.config.db_uri)
        except PyMongoError as exc:
            raise PyMongoError("Could not initialize the MongoDB repository") from exc

    def save_dataset(self, dataframe: pd.DataFrame, collection_name: str = "dataset") -> int:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("dataframe must be a pandas DataFrame")
        if not collection_name.strip():
            raise ValueError("collection_name must not be empty")
        if dataframe.empty:
            return 0

        records = dataframe.to_dict(orient="records")
        collection = self.client[self.config.db_name][collection_name]

        try:
            result = collection.insert_many(records)
        except PyMongoError as exc:
            raise PyMongoError(
                f"Could not save dataset to MongoDB collection '{collection_name}'"
            ) from exc

        return len(result.inserted_ids)

    def close(self) -> None:
        if self.client is not None:
            self.client.close()

    def __enter__(self) -> "MongoRepository":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

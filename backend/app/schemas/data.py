from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class DataRecordCreate(BaseModel):
    table_name: str
    data: Dict[str, Any]

class DataRecordUpdate(BaseModel):
    table_name: str
    data: Dict[str, Any]
    match_column: str = "id"
    match_value: Any

class DataQueryRequest(BaseModel):
    table_name: str
    columns: str = "*"
    filters: Optional[Dict[str, Any]] = None
    limit: Optional[int] = 100

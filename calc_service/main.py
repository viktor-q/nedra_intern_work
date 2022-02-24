from typing import List, Optional
import modules.simple_calc
import modules.storage
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class CalcRequestDTO(BaseModel):
    input_data: str

    class Config:
        schema_extra = {"example": {"input_data": "7+5"}}


class CalcResponseDTO(BaseModel):
    output_data: str

    class Config:
        schema_extra = {"example": {"output_data": "13.234"}}


@app.post("/calc", response_model=CalcResponseDTO)
async def calculation(pushed_data: CalcRequestDTO):
    storager = modules.storage.StorageInJson()
    try:
        calculator = modules.simple_calc.SimpleCalculator()
        result = calculator.calculation_from_string(pushed_data.input_data)

        storager = modules.storage.StorageInJson()
        storager.add_log_to_json(pushed_data.input_data, result)

        return {"output_data": result}

    except modules.simple_calc.NotValidFirstSymbol:
        storager.add_log_to_json(pushed_data.input_data, "error")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not Valid First Symbol"
        )
    except modules.simple_calc.NotValidOperators:
        storager.add_log_to_json(pushed_data.input_data, "error")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Valid Operators")
    except modules.simple_calc.NotIdentifiedErrorInCalc:
        storager.add_log_to_json(pushed_data.input_data, "error")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not Identified Error In Module Calc"
        )


class HistoryRequestDTO(BaseModel):
    limit: Optional[int] = None
    status: Optional[str] = None

    class Config:
        schema_extra = {"example": {"limit": 5, "status": "fail"}}


class HistoryResponseDTO(BaseModel):
    request: str
    response: str
    status: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": [{"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}]
        }


@app.post("/history", response_model=List[HistoryResponseDTO])
async def history(pushed_data: HistoryRequestDTO):
    try:
        logs = modules.storage.StorageInJson()
        result_history = logs.read_log_from_json(pushed_data.limit, pushed_data.status)
        return result_history
    except modules.storage.NotValidLimit:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Valid Limit")
    except modules.storage.NotValidStatus:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Valid Status")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

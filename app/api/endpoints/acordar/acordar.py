from fastapi import APIRouter

router = APIRouter()

@router.get("/acordar")
def acordar():
    return "só mais 5 min, mae"

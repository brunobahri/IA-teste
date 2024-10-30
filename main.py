from fastapi import FastAPI, HTTPException
import ollama

app = FastAPI()

@app.get("/")
def root():
    try:
        response = ollama.chat(model="tinyllama", messages=[
            {"role": "user", "content": "What's 2+2?"},
        ])
        llm_res = response.get('message', {}).get('content', '')
        return {"response": llm_res}
    except ollama._types.ResponseError as e:
        # Erros específicos do Ollama (por exemplo, modelo não encontrado)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Outros erros genéricos
        raise HTTPException(status_code=500, detail=str(e))

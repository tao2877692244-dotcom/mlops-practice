from fastapi import FastAPI

# 初始化服务引擎
app = FastAPI()

# 接口 1：当你访问根目录 / 时，返回欢迎信息
@app.get("/")
def read_root():
    return {"message": "Hello MLOps! The model is ready."}

# 接口 2：当你访问 /predict 时，接收数据并计算结果
@app.post("/predict")
def predict(data: dict):
    # data 是你从浏览器传进来的 JSON 数据，比如 {"a": 10, "b": 20}
    # 逻辑：把 a 和 b 加起来
    result = data["a"] + data["b"]
    return {"result": result}

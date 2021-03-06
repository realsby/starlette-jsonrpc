import uvicorn
from starlette.applications import Starlette

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint

app = Starlette()


@dispatcher.add_method
async def subtract(params):
    return params["x"] - params["y"]


@dispatcher.add_method(name="SubtractMethod")
async def seconds_subtract(params):
    return params["x"] - params["y"]


app.mount("/api", JSONRPCEndpoint)


if __name__ == "__main__":
    uvicorn.run(app)

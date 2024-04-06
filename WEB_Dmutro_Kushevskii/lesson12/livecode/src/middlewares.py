
async def printer_middleware(request, call_next):
    print(1)
    response = await call_next(request)
    return response

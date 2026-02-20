
def handle_request(request):
    match request:
        case {"status": 200, "data": [*items]} if len(items) > 0:
            return f"Processed {len(items)} items."
        case {"status": 404}:
            return "Not Found"
        case _:
            return "Unknown Error"

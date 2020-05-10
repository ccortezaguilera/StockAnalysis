def get_page_size(request):
    return request.args.get("size", 10)


def get_page(request):
    return request.args.get("page", 1)


def get_max_results_size(size: int, page: int):
    return size * page


def get_date_start(request):
    return request.args.get("date_start")


def get_date_end(request):
    return request.args.get("date_end")

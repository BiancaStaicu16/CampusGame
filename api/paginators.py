from rest_framework.pagination import LimitOffsetPagination


def paginate_data(request, data):
    """
    Paginate data using DRF LimitOffset paginator.
    Get the data calling '.data'.
    :param request: session request.
    :param data: queryset.
    :return: paginated data as:
        {
            "count": *int*,
            "next": *link_to_next_page*,
            "previous": *link_to_previous_page*,
            "results": [ *data_from_queryset* ]
        }
    """
    paginator = LimitOffsetPagination()
    page = paginator.paginate_queryset(data, request)
    if page is not None:
        return paginator.get_paginated_response(page)
    return data

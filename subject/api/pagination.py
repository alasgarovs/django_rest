from rest_framework.pagination import PageNumberPagination

class LargePagination(PageNumberPagination):
    page_size = 2
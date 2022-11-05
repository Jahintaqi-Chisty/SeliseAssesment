from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    """
	Added Page Size insted of size and for page_size_query_param limit the  record if we pass page_size in params
    """
    # size = 2
    # size_query_param = 'page_size'
    
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

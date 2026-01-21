from django.http import HttpRequest

class RequestUtil:
    """
    Author: 김대광
    """

    _is_null = "{} is null"

    @classmethod
    def get_request_ip_address(cls, request: HttpRequest) -> str:
        """IP 주소 가져오기

        Args:
            request (HttpRequest): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip
    
    @classmethod
    def get_request_domain(cls, request: HttpRequest) -> str:
        """포트와 컨텍스트 경로를 포함한 전체 베이스 URL 가져오기

        Args:
            request (HttpRequest): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        scheme = request.is_secure() and "https" or "http"
        host = request.get_host()

        return f"{scheme}://{host}"
    
    @classmethod
    def get_base_domain(cls, request: HttpRequest) -> str:
        """기본 도메인 가져오기 (포트 미포함, 호스트명만)

        Args:
            request (HttpRequest): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        scheme = request.is_secure() and "https" or "http"
        host = request.get_host().split(':')[0]

        return f"{scheme}://{host}"
    
    @classmethod
    def get_browser_info(cls, request: HttpRequest) -> str:
        """브라우저 User-Agent 가져오기

        Args:
            request (HttpRequest): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        
        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        user_agent = request.META.get('HTTP_USER_AGENT', 'User-Agent 정보 없음')
        return user_agent

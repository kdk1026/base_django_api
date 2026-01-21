from django.http import HttpRequest
from typing import Any, Optional

class SessionUtil:
    """
    Author: 김대광
    """

    _is_null = "{} is null"
    _is_null_or_empty = "{} is null or empty"
    _is_negative = "{} is negative"

    @classmethod
    def set_attribute(cls, request: HttpRequest, key: str, value: Any, timeout: Optional[int] = None) -> None:
        """세션에 데이터 저장

        Args:
            request (HttpRequest): _description_
            key (str): _description_
            value (Any): _description_
            timeout (Optional[int], optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        if value is None:
            raise ValueError(cls._is_null.format("value"))
        
        request.session[key] = value

        if timeout is not None:
            if timeout < 1:
                raise ValueError(cls._is_negative.format("timeout"))
            request.session.set_expiry(timeout)
    
    @classmethod
    def get_attribute(cls, request: HttpRequest, key: str) -> Any:
        """세션에서 데이터 가져오기

        Args:
            request (HttpRequest): _description_
            key (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            Any: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        return request.session.get(key)
    
    @classmethod
    def remove_attribute(cls, request: HttpRequest, key: str) -> None:
        """특정 세션 키 삭제

        Args:
            request (HttpRequest): _description_
            key (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))
        
        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        if key in request.session:
            del request.session[key]
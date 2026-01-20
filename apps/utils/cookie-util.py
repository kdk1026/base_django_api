from dataclasses import dataclass
from django.http import HttpRequest, HttpResponse
from typing import Optional


@dataclass
class CookieConfig:
    name: str
    value: str = ""
    expiry: Optional[int] = None
    domain: Optional[str] = None
    profile: str = "local"

class CookieUtil:
    """
    Author: 김대광
    """

    _is_null = "{} is null"
    _is_null_or_empty = "{} is null or empty"
    _is_negative = "{} is negative"

    _LOCAL_PROFILE = "local"
    _COOKIE_NAME = "config.name"

    @classmethod
    def add_cookie(cls, response: HttpResponse, config: CookieConfig) -> None:
        """쿠키 설정

        Args:
            response (HttpResponse): _description_
            config (CookieConfig): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """

        if not response:
            raise ValueError(cls._is_null.format("response"))

        if not config.name or not config.name.strip():
            raise ValueError(cls._is_null_or_empty.format(cls._COOKIE_NAME))

        if not config.value or not config.value.strip():
            raise ValueError(cls._is_null_or_empty.format("config.value"))
        
        if config.expiry < 0:
            raise ValueError(cls._is_negative.format("config.expiry"))
        
        response.set_cookie(
            key=config.name,
            value=config.value,
            max_age=config.expiry,
            path='/',
            domain=config.domain,
            secure=config.profile != cls._LOCAL_PROFILE,
            httponly=True,
        )

    @classmethod
    def add_session_cookie(cls, response: HttpResponse, config: CookieConfig) -> None:
        """세션 쿠키 설정

        Args:
            response (HttpResponse): _description_
            config (CookieConfig): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """

        if not response:
            raise ValueError(cls._is_null.format("response"))

        if not config.name or not config.name.strip():
            raise ValueError(cls._is_null_or_empty.format(cls._COOKIE_NAME))

        if not config.value or not config.value.strip():
            raise ValueError(cls._is_null_or_empty.format("config.value"))
        
        response.set_cookie(
            key=config.name,
            value=config.value,
            max_age=None,
            path='/',
            domain=config.domain,
            secure=config.profile != cls._LOCAL_PROFILE,
            httponly=True,
        )

    @classmethod
    def get_cookie_value(cls, request: HttpRequest, cookie_name: str) -> str:
        """쿠키 값 가져오기

        Args:
            request (HttpRequest): _description_
            cookie_name (str): _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))

        if not cookie_name or not cookie_name.strip():
            raise ValueError(cls._is_null_or_empty.format("cookie_name"))
        
        return request.COOKIES.get(cookie_name, "")
    
    @classmethod
    def remove_cookie(cls, response: HttpResponse, config: CookieConfig) -> None:
        """특정 쿠키 제거

        Args:
            response (HttpResponse): _description_
            config (CookieConfig): _description_
        """
        
        if not response:
            raise ValueError(cls._is_null.format("response"))

        if not config.name or not config.name.strip():
            raise ValueError(cls._is_null_or_empty.format(cls._COOKIE_NAME))
        
        response.delete_cookie(
            key=config.name,
            domain=config.domain,
            path='/'
        )

    @classmethod
    def is_exist(cls, request: HttpRequest, cookie_name: str) -> bool:
        """쿠키 존재 여부 확인

        Args:
            request (HttpRequest): _description_
            cookie_name (str): _description_

        Returns:
            bool: _description_
        """

        if not request:
            raise ValueError(cls._is_null.format("request"))

        if not cookie_name or not cookie_name.strip():
            raise ValueError(cls._is_null_or_empty.format("cookie_name"))
        
        return cookie_name in request.COOKIES
"""
Configuration management for Site24x7 CLI
"""

import os
from typing import Optional

class Config:
    """CLI configuration"""
    
    DEFAULT_BASE_URL = 'https://www.site24x7.com/api'
    DEFAULT_OUTPUT_FORMAT = 'table'
    
    @classmethod
    def get_oauth_token(cls) -> Optional[str]:
        """Get OAuth token from environment or config"""
        return os.getenv('SITE24X7_OAUTH_TOKEN')
    
    @classmethod
    def get_base_url(cls) -> str:
        """Get API base URL"""
        return os.getenv('SITE24X7_BASE_URL', cls.DEFAULT_BASE_URL)
    
    @classmethod
    def get_output_format(cls) -> str:
        """Get default output format"""
        return os.getenv('SITE24X7_OUTPUT_FORMAT', cls.DEFAULT_OUTPUT_FORMAT)

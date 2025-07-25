"""
Utility functions for Site24x7 CLI
"""

import json
import re
from typing import Any, Dict, List
from datetime import datetime

def validate_monitor_id(monitor_id: str) -> bool:
    """Validate monitor ID format"""
    return bool(re.match(r'^[0-9]+$', monitor_id))

def format_timestamp(timestamp: str) -> str:
    """Format timestamp for display"""
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        return timestamp

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for file operations"""
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)

def parse_key_value_pairs(pairs: List[str]) -> Dict[str, str]:
    """Parse key=value pairs from command line"""
    result = {}
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            result[key.strip()] = value.strip()
    return result

"""
Base classes for Site24x7 CLI
"""

import json
import os
from typing import Dict, Any, Optional
import click
import requests
from rich.console import Console
from rich.table import Table

console = Console()

class Site24x7Client:
    """Base client for Site24x7 API interactions"""
    
    def __init__(self, oauth_token: str = None):
        self.oauth_token = oauth_token or os.getenv('SITE24X7_OAUTH_TOKEN')
        self.base_url = 'https://www.site24x7.com/api'
        self.session = requests.Session()
        
        if self.oauth_token:
            self.session.headers.update({
                'Authorization': f'Zoho-oauthtoken {self.oauth_token}',
                'Accept': 'application/json; version=2.0',
                'Content-Type': 'application/json;charset=UTF-8'
            })
    
    def request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make API request"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            console.print(f"[red]API Error: {e}[/red]")
            raise
    
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """GET request"""
        return self.request('GET', endpoint, **kwargs)
    
    def post(self, endpoint: str, data: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        """POST request"""
        return self.request('POST', endpoint, json=data, **kwargs)
    
    def put(self, endpoint: str, data: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        """PUT request"""
        return self.request('PUT', endpoint, json=data, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """DELETE request"""
        return self.request('DELETE', endpoint, **kwargs)

class BaseCommand:
    """Base class for all CLI commands"""
    
    def __init__(self):
        self.client = Site24x7Client()
    
    def format_output(self, data: Any, output_format: str = 'table') -> None:
        """Format and display output"""
        if output_format == 'json':
            console.print_json(json.dumps(data, indent=2))
        elif output_format == 'table' and isinstance(data, list):
            self._display_table(data)
        else:
            console.print(data)
    
    def _display_table(self, data: List[Dict[str, Any]]) -> None:
        """Display data as a rich table"""
        if not data:
            console.print("[yellow]No data to display[/yellow]")
            return
        
        table = Table()
        
        # Add columns from first item keys
        for key in data[0].keys():
            table.add_column(key.replace('_', ' ').title())
        
        # Add rows
        for item in data:
            table.add_row(*[str(value) for value in item.values()])
        
        console.print(table)

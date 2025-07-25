"""
Authentication module for Site24x7 CLI
"""

import os
import json
from typing import Optional
import click
from rich.console import Console

console = Console()

class AuthManager:
    """Manage authentication credentials"""
    
    CONFIG_FILE = os.path.expanduser('~/.site24x7/credentials.json')
    
    @classmethod
    def save_credentials(cls, oauth_token: str) -> None:
        """Save OAuth token to config file"""
        os.makedirs(os.path.dirname(cls.CONFIG_FILE), exist_ok=True)
        
        config = {
            'oauth_token': oauth_token,
            'saved_at': str(datetime.utcnow())
        }
        
        with open(cls.CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print("[green]Credentials saved successfully[/green]")
    
    @classmethod
    def load_credentials(cls) -> Optional[str]:
        """Load OAuth token from config file"""
        if os.path.exists(cls.CONFIG_FILE):
            try:
                with open(cls.CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    return config.get('oauth_token')
            except Exception as e:
                console.print(f"[red]Error loading credentials: {e}[/red]")
        
        return None
    
    @classmethod
    def clear_credentials(cls) -> None:
        """Clear saved credentials"""
        if os.path.exists(cls.CONFIG_FILE):
            os.remove(cls.CONFIG_FILE)
            console.print("[green]Credentials cleared[/green]")

@click.command()
@click.option('--token', required=True, help='Site24x7 OAuth token')
def configure(token: str):
    """Configure Site24x7 CLI with OAuth token"""
    AuthManager.save_credentials(token)

@click.command()
def clear():
    """Clear saved credentials"""
    AuthManager.clear_credentials()

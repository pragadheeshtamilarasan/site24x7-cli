#!/usr/bin/env python3
"""
Site24x7 CLI - Site24x7 CLI - Comprehensive monitoring and management tool
Version: 1.20250725.1943
Generated automatically by AI from Site24x7 API documentation

This CLI provides comprehensive access to all Site24x7 monitoring and management capabilities.
"""

import os
import sys
import json
import click
from typing import Dict, Any, Optional

# Import base classes and utilities
from site24x7_cli.base import Site24x7Client, BaseCommand
from site24x7_cli.auth import AuthManager
from site24x7_cli.config import Config
from site24x7_cli.exceptions import Site24x7CLIError, AuthenticationError

# Import command modules

from site24x7_cli.commands.monitor-management import monitor-management_group

from site24x7_cli.commands.reports import reports_group



@click.group(name='site24x7')
@click.version_option(version='1.20250725.1943')
@click.option('--config', '-c', help='Configuration file path')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml']), 
              default='table', help='Output format')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--token', help='Site24x7 OAuth token (overrides config)')
@click.pass_context
def cli(ctx, config, output, verbose, token):
    """
    Site24x7 CLI - Comprehensive monitoring and management tool
    
    A comprehensive command-line interface for Site24x7 monitoring platform.
    Provides access to all monitoring, reporting, and management features.
    
    Examples:
        site24x7 monitors list                    # List all monitors
        site24x7 monitors website create --help   # Get help for website monitor creation
        site24x7 reports performance --monitor-id 123456  # Get performance report
        site24x7 auth configure --token YOUR_TOKEN        # Configure authentication
    
    Visit https://github.com/site24x7/site24x7-cli for documentation and examples.
    """
    # Ensure context object exists
    ctx.ensure_object(dict)
    
    # Store global options
    ctx.obj['output_format'] = output
    ctx.obj['verbose'] = verbose
    ctx.obj['config_file'] = config
    
    # Setup authentication
    oauth_token = token or AuthManager.load_credentials() or os.getenv('SITE24X7_OAUTH_TOKEN')
    
    if not oauth_token:
        # Only require token for non-auth commands
        if ctx.invoked_subcommand not in ['auth', 'configure']:
            click.echo(click.style('Error: No OAuth token provided.', fg='red'), err=True)
            click.echo('Run "site24x7 auth configure" to set up authentication.', err=True)
            sys.exit(1)
    else:
        ctx.obj['oauth_token'] = oauth_token
    
    # Setup verbose logging
    if verbose:
        import logging
        logging.basicConfig(level=logging.DEBUG)


# Authentication commands
@cli.group()
def auth():
    """Authentication and configuration management"""
    pass


@auth.command()
@click.option('--token', prompt=True, hide_input=True, 
              help='Site24x7 OAuth token')
def configure(token):
    """Configure Site24x7 CLI with OAuth token"""
    try:
        # Validate token format (basic check)
        if not token or len(token) < 20:
            raise click.BadParameter('Invalid token format')
        
        # Test token by making a simple API call
        client = Site24x7Client(token)
        try:
            # Try to get current status to validate token
            response = client.get('/current_status')
            click.echo(click.style('✓ Token validated successfully', fg='green'))
        except Exception as e:
            click.echo(click.style(f'⚠ Warning: Could not validate token: {e}', fg='yellow'))
            click.echo('Token saved but may not be valid.')
        
        # Save credentials
        AuthManager.save_credentials(token)
        click.echo(click.style('✓ Configuration saved', fg='green'))
        
    except Exception as e:
        click.echo(click.style(f'Error: {e}', fg='red'), err=True)
        sys.exit(1)


@auth.command()
def clear():
    """Clear saved authentication credentials"""
    AuthManager.clear_credentials()


@auth.command()
def status():
    """Show authentication status"""
    token = AuthManager.load_credentials()
    if token:
        masked_token = f"***{token[-8:]}" if len(token) > 8 else "***"
        click.echo(f"Status: Configured (Token: {masked_token})")
        
        # Test connection
        try:
            client = Site24x7Client(token)
            response = client.get('/current_status')
            click.echo(click.style('✓ Connection: Active', fg='green'))
        except Exception as e:
            click.echo(click.style(f'✗ Connection: Failed ({e})', fg='red'))
    else:
        click.echo("Status: Not configured")
        click.echo("Run 'site24x7 auth configure' to set up authentication.")


# Add command groups

cli.add_command(monitor-management_group)

cli.add_command(reports_group)



# Global error handler
def handle_api_error(e: Exception) -> None:
    """Handle API errors consistently"""
    if isinstance(e, AuthenticationError):
        click.echo(click.style('Authentication failed. Please check your OAuth token.', fg='red'), err=True)
        click.echo('Run "site24x7 auth configure" to update your credentials.', err=True)
    elif isinstance(e, Site24x7CLIError):
        click.echo(click.style(f'Site24x7 CLI Error: {e}', fg='red'), err=True)
    else:
        click.echo(click.style(f'Unexpected error: {e}', fg='red'), err=True)


# Utility function for consistent output formatting
def format_output(data: Any, output_format: str = 'table') -> None:
    """Format and display output consistently"""
    if output_format == 'json':
        click.echo(json.dumps(data, indent=2, default=str))
    elif output_format == 'yaml':
        try:
            import yaml
            click.echo(yaml.dump(data, default_flow_style=False))
        except ImportError:
            click.echo('YAML output requires PyYAML. Install with: pip install PyYAML')
            click.echo(json.dumps(data, indent=2, default=str))
    else:
        # Table format - handled by individual commands
        click.echo(data)


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        click.echo('\nAborted.', err=True)
        sys.exit(1)
    except Exception as e:
        handle_api_error(e)
        sys.exit(1)
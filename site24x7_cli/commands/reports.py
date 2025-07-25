"""
Site24x7 CLI - Reports Commands
Generated automatically from Site24x7 API documentation

This module provides CLI commands for Manage Reports.
"""

import click
import json
from typing import Dict, Any, Optional, List
from rich.console import Console
from rich.table import Table

from site24x7_cli.base import BaseCommand, Site24x7Client
from site24x7_cli.exceptions import Site24x7CLIError, APIError
from site24x7_cli.utils import validate_monitor_id, format_timestamp, parse_key_value_pairs

console = Console()


class ReportsCommand(BaseCommand):
    """Base command class for reports operations"""
    
    def __init__(self):
        super().__init__()
        self.category = "reports"


@click.group(name='reports')
@click.pass_context
def reports_group(ctx):
    """Manage Reports management commands"""
    pass



@reports_group.group(name='performance-reports')
@click.pass_context
def performance-reports_group(ctx):
    """Manage Performance Reports operations"""
    pass



@performance-reports_group.command(name='list')

@click.option('--limit', '-l', type=int, default=50, help='Number of items to retrieve')
@click.option('--offset', type=int, default=0, help='Offset for pagination')
@click.option('--status', type=click.Choice(['up', 'down', 'trouble', 'critical', 'suspended']), 
              help='Filter by status')
@click.option('--group-id', type=str, help='Filter by monitor group ID')

@click.pass_context
def list(ctx, **kwargs):
    """List all Performance Reports"""
    try:
        command = ReportsCommand()
        result = command.list_performance-reports(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@performance-reports_group.command(name='get')

@click.argument('id', required=True)

@click.pass_context
def get(ctx, **kwargs):
    """Get specific Performance Reports by ID"""
    try:
        command = ReportsCommand()
        result = command.get_performance-reports(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@performance-reports_group.command(name='create')

@click.option('--name', '-n', required=True, help='Performance-Reports name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def create(ctx, **kwargs):
    """Create new Performance Reports"""
    try:
        command = ReportsCommand()
        result = command.create_performance-reports(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@performance-reports_group.command(name='update')

@click.argument('id', required=True)
@click.option('--name', '-n', help='New name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def update(ctx, **kwargs):
    """Update Performance Reports"""
    try:
        command = ReportsCommand()
        result = command.update_performance-reports(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@performance-reports_group.command(name='delete')

@click.argument('id', required=True)
@click.option('--force', '-f', is_flag=True, help='Force deletion without confirmation')

@click.pass_context
def delete(ctx, **kwargs):
    """Delete Performance Reports"""
    try:
        command = ReportsCommand()
        result = command.delete_performance-reports(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))





# Implementation methods for ReportsCommand class


    def list_performance-reports(self, limit: int = 50, offset: int = 0, 
                                  status: Optional[str] = None, 
                                  group_id: Optional[str] = None, **kwargs) -> List[Dict[str, Any]]:
        """List performance-reports"""
        params = {'limit': limit, 'offset': offset}
        
        if status:
            params['status'] = status
        if group_id:
            params['group_id'] = group_id
        
        endpoint = "/api/performance-reports"
        response = self.client.get(endpoint, params=params)
        
        if 'data' in response:
            return response['data']
        return response.get('performance-reports', [])

    def get_performance-reports(self, id: str, **kwargs) -> Dict[str, Any]:
        """Get specific performance-reports by ID"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        endpoint = f"/api/performance-reports/{id}"
        response = self.client.get(endpoint)
        
        if 'data' in response:
            return response['data']
        return response

    def create_performance-reports(self, name: str, config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Create new performance-reports"""
        data = {'display_name': name}
        
        # Load configuration from file if provided
        if config:
            config_data = json.load(config)
            data.update(config_data)
        
        # Parse additional parameters
        if param:
            additional_params = parse_key_value_pairs(param)
            data.update(additional_params)
        
        # Add default required fields based on monitor type
        if 'monitor' in "performance-reports":
            data.setdefault('monitor_type', 'PERFORMANCE-REPORTS')
            data.setdefault('check_frequency', '5')
            data.setdefault('timeout', '30')
        
        endpoint = "/api/performance-reports"
        response = self.client.post(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def update_performance-reports(self, id: str, name: Optional[str] = None, 
                                    config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Update performance-reports"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        data = {}
        
        if name:
            data['display_name'] = name
        
        # Load configuration from file if provided
        if config:
            config_data = json.load(config)
            data.update(config_data)
        
        # Parse additional parameters
        if param:
            additional_params = parse_key_value_pairs(param)
            data.update(additional_params)
        
        if not data:
            raise ValueError("No update parameters provided")
        
        endpoint = f"/api/performance-reports/{id}"
        response = self.client.put(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def delete_performance-reports(self, id: str, force: bool = False, **kwargs) -> Dict[str, Any]:
        """Delete performance-reports"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        if not force:
            click.confirm(f'Are you sure you want to delete performance-reports {id}?', abort=True)
        
        endpoint = f"/api/performance-reports/{id}"
        response = self.client.delete(endpoint)
        
        return response



# Add methods to the command class

setattr(ReportsCommand, 'list_performance-reports', 
        ReportsCommand.__dict__['list_performance-reports'])
setattr(ReportsCommand, 'get_performance-reports', 
        ReportsCommand.__dict__['get_performance-reports'])
setattr(ReportsCommand, 'create_performance-reports', 
        ReportsCommand.__dict__['create_performance-reports'])
setattr(ReportsCommand, 'update_performance-reports', 
        ReportsCommand.__dict__['update_performance-reports'])
setattr(ReportsCommand, 'delete_performance-reports', 
        ReportsCommand.__dict__['delete_performance-reports'])


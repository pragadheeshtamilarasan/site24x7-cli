"""
Site24x7 CLI - Monitor-Management Commands
Generated automatically from Site24x7 API documentation

This module provides CLI commands for Manage Monitor Management.
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


class Monitor-ManagementCommand(BaseCommand):
    """Base command class for monitor-management operations"""
    
    def __init__(self):
        super().__init__()
        self.category = "monitor-management"


@click.group(name='monitor-management')
@click.pass_context
def monitor-management_group(ctx):
    """Manage Monitor Management management commands"""
    pass



@monitor-management_group.group(name='website-monitors')
@click.pass_context
def website-monitors_group(ctx):
    """Manage Website Monitors operations"""
    pass



@website-monitors_group.command(name='list')

@click.option('--limit', '-l', type=int, default=50, help='Number of items to retrieve')
@click.option('--offset', type=int, default=0, help='Offset for pagination')
@click.option('--status', type=click.Choice(['up', 'down', 'trouble', 'critical', 'suspended']), 
              help='Filter by status')
@click.option('--group-id', type=str, help='Filter by monitor group ID')

@click.pass_context
def list(ctx, **kwargs):
    """List all Website Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.list_website-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@website-monitors_group.command(name='get')

@click.argument('id', required=True)

@click.pass_context
def get(ctx, **kwargs):
    """Get specific Website Monitors by ID"""
    try:
        command = Monitor-ManagementCommand()
        result = command.get_website-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@website-monitors_group.command(name='create')

@click.option('--name', '-n', required=True, help='Website-Monitors name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def create(ctx, **kwargs):
    """Create new Website Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.create_website-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@website-monitors_group.command(name='update')

@click.argument('id', required=True)
@click.option('--name', '-n', help='New name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def update(ctx, **kwargs):
    """Update Website Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.update_website-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@website-monitors_group.command(name='delete')

@click.argument('id', required=True)
@click.option('--force', '-f', is_flag=True, help='Force deletion without confirmation')

@click.pass_context
def delete(ctx, **kwargs):
    """Delete Website Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.delete_website-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))




@monitor-management_group.group(name='api-monitors')
@click.pass_context
def api-monitors_group(ctx):
    """Manage API Monitors operations"""
    pass



@api-monitors_group.command(name='list')

@click.option('--limit', '-l', type=int, default=50, help='Number of items to retrieve')
@click.option('--offset', type=int, default=0, help='Offset for pagination')
@click.option('--status', type=click.Choice(['up', 'down', 'trouble', 'critical', 'suspended']), 
              help='Filter by status')
@click.option('--group-id', type=str, help='Filter by monitor group ID')

@click.pass_context
def list(ctx, **kwargs):
    """List all API Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.list_api-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@api-monitors_group.command(name='get')

@click.argument('id', required=True)

@click.pass_context
def get(ctx, **kwargs):
    """Get specific API Monitors by ID"""
    try:
        command = Monitor-ManagementCommand()
        result = command.get_api-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@api-monitors_group.command(name='create')

@click.option('--name', '-n', required=True, help='Api-Monitors name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def create(ctx, **kwargs):
    """Create new API Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.create_api-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@api-monitors_group.command(name='update')

@click.argument('id', required=True)
@click.option('--name', '-n', help='New name')
@click.option('--config', '-c', type=click.File('r'), help='Configuration file (JSON)')
@click.option('--param', '-p', multiple=True, help='Parameters in key=value format')

@click.pass_context
def update(ctx, **kwargs):
    """Update API Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.update_api-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))



@api-monitors_group.command(name='delete')

@click.argument('id', required=True)
@click.option('--force', '-f', is_flag=True, help='Force deletion without confirmation')

@click.pass_context
def delete(ctx, **kwargs):
    """Delete API Monitors"""
    try:
        command = Monitor-ManagementCommand()
        result = command.delete_api-monitors(**kwargs)
        
        output_format = ctx.obj.get('output_format', 'table')
        command.format_output(result, output_format)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if ctx.obj.get('verbose'):
            import traceback
            console.print(f"[red]{traceback.format_exc()}[/red]")
        raise click.ClickException(str(e))





# Implementation methods for Monitor-ManagementCommand class


    def list_website-monitors(self, limit: int = 50, offset: int = 0, 
                                  status: Optional[str] = None, 
                                  group_id: Optional[str] = None, **kwargs) -> List[Dict[str, Any]]:
        """List website-monitors"""
        params = {'limit': limit, 'offset': offset}
        
        if status:
            params['status'] = status
        if group_id:
            params['group_id'] = group_id
        
        endpoint = "/api/website-monitors"
        response = self.client.get(endpoint, params=params)
        
        if 'data' in response:
            return response['data']
        return response.get('website-monitors', [])

    def get_website-monitors(self, id: str, **kwargs) -> Dict[str, Any]:
        """Get specific website-monitors by ID"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        endpoint = f"/api/website-monitors/{id}"
        response = self.client.get(endpoint)
        
        if 'data' in response:
            return response['data']
        return response

    def create_website-monitors(self, name: str, config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Create new website-monitors"""
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
        if 'monitor' in "website-monitors":
            data.setdefault('monitor_type', 'WEBSITE-MONITORS')
            data.setdefault('check_frequency', '5')
            data.setdefault('timeout', '30')
        
        endpoint = "/api/website-monitors"
        response = self.client.post(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def update_website-monitors(self, id: str, name: Optional[str] = None, 
                                    config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Update website-monitors"""
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
        
        endpoint = f"/api/website-monitors/{id}"
        response = self.client.put(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def delete_website-monitors(self, id: str, force: bool = False, **kwargs) -> Dict[str, Any]:
        """Delete website-monitors"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        if not force:
            click.confirm(f'Are you sure you want to delete website-monitors {id}?', abort=True)
        
        endpoint = f"/api/website-monitors/{id}"
        response = self.client.delete(endpoint)
        
        return response



    def list_api-monitors(self, limit: int = 50, offset: int = 0, 
                                  status: Optional[str] = None, 
                                  group_id: Optional[str] = None, **kwargs) -> List[Dict[str, Any]]:
        """List api-monitors"""
        params = {'limit': limit, 'offset': offset}
        
        if status:
            params['status'] = status
        if group_id:
            params['group_id'] = group_id
        
        endpoint = "/api/api-monitors"
        response = self.client.get(endpoint, params=params)
        
        if 'data' in response:
            return response['data']
        return response.get('api-monitors', [])

    def get_api-monitors(self, id: str, **kwargs) -> Dict[str, Any]:
        """Get specific api-monitors by ID"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        endpoint = f"/api/api-monitors/{id}"
        response = self.client.get(endpoint)
        
        if 'data' in response:
            return response['data']
        return response

    def create_api-monitors(self, name: str, config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Create new api-monitors"""
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
        if 'monitor' in "api-monitors":
            data.setdefault('monitor_type', 'API-MONITORS')
            data.setdefault('check_frequency', '5')
            data.setdefault('timeout', '30')
        
        endpoint = "/api/api-monitors"
        response = self.client.post(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def update_api-monitors(self, id: str, name: Optional[str] = None, 
                                    config: Optional[Any] = None, 
                                    param: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Update api-monitors"""
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
        
        endpoint = f"/api/api-monitors/{id}"
        response = self.client.put(endpoint, data=data)
        
        if 'data' in response:
            return response['data']
        return response

    def delete_api-monitors(self, id: str, force: bool = False, **kwargs) -> Dict[str, Any]:
        """Delete api-monitors"""
        if not validate_monitor_id(id):
            raise ValueError(f"Invalid ID format: {id}")
        
        if not force:
            click.confirm(f'Are you sure you want to delete api-monitors {id}?', abort=True)
        
        endpoint = f"/api/api-monitors/{id}"
        response = self.client.delete(endpoint)
        
        return response



# Add methods to the command class

setattr(Monitor-ManagementCommand, 'list_website-monitors', 
        Monitor-ManagementCommand.__dict__['list_website-monitors'])
setattr(Monitor-ManagementCommand, 'get_website-monitors', 
        Monitor-ManagementCommand.__dict__['get_website-monitors'])
setattr(Monitor-ManagementCommand, 'create_website-monitors', 
        Monitor-ManagementCommand.__dict__['create_website-monitors'])
setattr(Monitor-ManagementCommand, 'update_website-monitors', 
        Monitor-ManagementCommand.__dict__['update_website-monitors'])
setattr(Monitor-ManagementCommand, 'delete_website-monitors', 
        Monitor-ManagementCommand.__dict__['delete_website-monitors'])

setattr(Monitor-ManagementCommand, 'list_api-monitors', 
        Monitor-ManagementCommand.__dict__['list_api-monitors'])
setattr(Monitor-ManagementCommand, 'get_api-monitors', 
        Monitor-ManagementCommand.__dict__['get_api-monitors'])
setattr(Monitor-ManagementCommand, 'create_api-monitors', 
        Monitor-ManagementCommand.__dict__['create_api-monitors'])
setattr(Monitor-ManagementCommand, 'update_api-monitors', 
        Monitor-ManagementCommand.__dict__['update_api-monitors'])
setattr(Monitor-ManagementCommand, 'delete_api-monitors', 
        Monitor-ManagementCommand.__dict__['delete_api-monitors'])


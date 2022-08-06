import pandas as pd
from pandasql import sqldf
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import yaml
import sys
import os

dashboard = ' '.join(sys.argv[1:])

kakapo_home = os.environ.get('KAKAPO_HOME', os.environ.get('HOME') + '/kakapo')

with open(kakapo_home + '/dashboards/' + dashboard + ".yaml", "r") as stream:
  try:
    dashboard = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    exit(exc)


tables = {}
for d in dashboard['data']:
  tables[d] = pd.read_csv(kakapo_home + '/data/' + d + '.csv')

items = {}
for item in dashboard['items']:
  items[item['id']] = {
    'id': item['id'],
    'type': item['type'] if 'type' in item else 'table',
    'title': item['title'],
    'data': sqldf(item['query'], tables) 
  }


def create_renderable(item):
  if item['type'] == 'text':
    return Panel(str(item['data'].iloc[0, 0]), title=item['title'], title_align="left", box=box.SQUARE)
  
  table = Table(show_header=True, expand=True, box=box.MINIMAL)
  for column in list(item['data']):
    table.add_column(column)

  for row in item['data'].values:
    table.add_row(*map(lambda x: str(x), row))

  return Panel(table, title=item['title'], title_align="left", box=box.SQUARE)


console = Console()

for row in dashboard['layout']:
  row_items = []
  for column in row['row']:

    stack_table = Table.grid(expand=True)

    for item in column['items']:
      stack_table.add_row(create_renderable(items[item]))

    row_items.append(stack_table)

  row_table = Table.grid(expand=True)
  row_table.add_row(*row_items)

  console.print()
  console.print(row_table)

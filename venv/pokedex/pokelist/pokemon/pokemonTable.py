from table import Table
from table.columns import Column
from .pokemon import Pokemon


class PokemonTable(Table):
    name = Column(field='name', header="Name")
    type_1 = Column(field='type_1', header="Type 1")
    type_2 = Column(field='type_1', header="Type 2")
    total = Column(field='total', header="Total")

    class Meta:
        model = Pokemon
    

from orator.migrations import Migration


class CreateTablePubliciones(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('publicaciones') as table:
            table.increments('id')
            table.string('titulo')
            table.string('descripcion')
            table.string('etiquetas')
            table.integer('creador')
            #table.string('latlng')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('publicaciones')

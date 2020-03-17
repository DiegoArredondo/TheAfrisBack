from orator.migrations import Migration


class CreateTableEventos(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('eventos') as table:
            table.increments('id')
            table.string('titulo')
            table.string('descripcion')
            table.string('etiquetas')
            table.timestamp('fechaHora')
            table.string('duracion')
            table.integer('cupo')
            table.string('ubicacion')
            table.integer('creador')
            #table.string('latlng')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('eventos')

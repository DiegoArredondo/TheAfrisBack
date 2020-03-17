from orator.migrations import Migration


class CreateTableUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('nombre')
            table.string('apellidos')
            table.string('correo')
            table.string('password')
            table.string('fechaNacimiento')
            table.string('descripcion')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')

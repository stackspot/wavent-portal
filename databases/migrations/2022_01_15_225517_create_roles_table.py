"""CreateRolesTable Migration."""

from masoniteorm.migrations import Migration


class CreateRolesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("roles") as table:
            table.increments("id")
            table.string("name", 50)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("roles")

"""CreatePermissionsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePermissionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("permissions") as table:
            table.increments("id")
            table.string("name", 50)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("permissions")

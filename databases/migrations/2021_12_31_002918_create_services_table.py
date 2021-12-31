"""CreateServicesTable Migration."""

from masoniteorm.migrations import Migration


class CreateServicesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("services") as table:
            table.increments("id")
            table.string("name")
            table.decimal("price", 10, 2)
            table.time("duration").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("services")

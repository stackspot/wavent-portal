"""CreateAccountsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("accounts") as table:
            table.increments("id").primary()
            table.string("name")
            table.string("slug").unique()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("accounts")

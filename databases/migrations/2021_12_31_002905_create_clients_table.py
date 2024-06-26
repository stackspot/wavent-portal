"""CreateClientsTable Migration."""

from masoniteorm.migrations import Migration


class CreateClientsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("clients") as table:
            table.increments("id").primary()
            table.string("name", 128).nullable()
            table.string("email", 128).nullable()
            table.string("phone", 50).nullable()
            table.unsigned("account_id").index()
            table.foreign("account_id").references("id").on("accounts").on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("clients")

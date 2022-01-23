"""AddAccountIdFieldInUsersTable Migration."""

from masoniteorm.migrations import Migration


class AddAccountIdFieldInUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.unsigned("account_id").index().after("phone")
            table.foreign("account_id").references("id").on("accounts").on_delete("cascade")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("account_id")

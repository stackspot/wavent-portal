"""CreateAccountUserPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountUserPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("account_user") as table:
            table.increments("id")
            table.unsigned('account_id')
            table.unsigned('user_id')
            table.foreign('account_id').references('id').on('accounts').on_delete('cascade')
            table.foreign('user_id').references('id').on('users').on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("account_user")

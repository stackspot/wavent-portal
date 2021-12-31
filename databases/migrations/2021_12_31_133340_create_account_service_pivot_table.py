"""CreateAccountServicePivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountServicePivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("account_service") as table:
            table.increments("id")
            table.unsigned("account_id")
            table.unsigned("service_id")
            table.foreign("account_id").references("id").on("accounts").on_delete("cascade")
            table.foreign("service_id").references("id").on("services").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("account_service")

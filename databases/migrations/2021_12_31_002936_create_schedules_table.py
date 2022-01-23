"""CreateSchedulesTable Migration."""

from masoniteorm.migrations import Migration


class CreateSchedulesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("schedules") as table:
            table.increments("id").primary()
            table.string("name")
            table.timestamp("start_time")
            table.timestamp("finish_time")
            table.boolean("is_working").default(True)
            table.unsigned("account_id").index()
            table.foreign("account_id").references("id").on("accounts").on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("schedules")

"""CreateSchedulesTable Migration."""

from masoniteorm.migrations import Migration


class CreateSchedulesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("schedules") as table:
            table.increments("id").primary()
            table.datetime("start_time")
            table.datetime("finish_time")
            table.boolean("is_working").default(True)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("schedules")

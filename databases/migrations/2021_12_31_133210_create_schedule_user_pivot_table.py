"""CreateScheduleUserPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateScheduleUserPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("schedule_user") as table:
            table.increments("id")
            table.unsigned("schedule_id")
            table.unsigned("user_id")
            table.foreign("schedule_id").references("id").on("schedules").on_delete("cascade")
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("schedule_user")

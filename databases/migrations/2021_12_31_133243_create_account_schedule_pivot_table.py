"""CreateAccountSchedulePivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountSchedulePivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("account_schedule") as table:
            table.increments("id")
            table.unsigned('account_id')
            table.unsigned('schedule_id')
            table.foreign('account_id').references('id').on('accounts').on_delete('cascade')
            table.foreign('schedule_id').references('id').on('schedules').on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("account_schedule")

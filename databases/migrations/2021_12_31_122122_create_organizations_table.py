"""CreateOrganizationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateOrganizationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("organizations") as table:
            table.increments("id")
            table.string("name", 128)
            table.string("email", 100).nullable()
            table.string("phone", 50).nullable()
            table.string("address", 150).nullable()
            table.string("city", 50).nullable()
            table.string("region", 50).nullable()
            table.string("country", 2).nullable()
            table.string("postal_code", 25).nullable()
            table.text("description").nullable()
            table.string("logo").nullable()
            table.string("brand_image").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("organizations")
